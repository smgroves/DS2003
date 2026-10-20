-- Screenshot Hunt: one-time Supabase setup.
-- Paste this whole file into Supabase → SQL Editor → Run.
-- Then set your host PIN with the last statement (edit it first!).

-- ---------- tables ----------
create table if not exists hunt_rounds (
  id          bigint generated always as identity primary key,
  prompt      text not null,
  seconds     int,                                -- null = no time limit
  started_at  timestamptz not null default now(),
  open        boolean not null default true
);

create table if not exists hunt_submissions (
  id          bigint generated always as identity primary key,
  round_id    bigint not null references hunt_rounds(id) on delete cascade,
  name        text not null check (char_length(name) between 1 and 40),
  path        text not null,
  created_at  timestamptz not null default now(),
  status      text not null default 'pending'
              check (status in ('pending', 'approved', 'rejected'))
);

create table if not exists hunt_secret (pin text not null);

alter table hunt_rounds      enable row level security;
alter table hunt_submissions enable row level security;
alter table hunt_secret      enable row level security;   -- no policies: unreadable from the browser

-- Newer Supabase projects don't grant table access to the browser role by default.
grant select on hunt_rounds, hunt_submissions to anon;

-- Anyone can see the current prompt; only approved screenshots are publicly readable.
drop policy if exists "read rounds" on hunt_rounds;
create policy "read rounds" on hunt_rounds for select to anon using (true);
drop policy if exists "read approved" on hunt_submissions;
create policy "read approved" on hunt_submissions for select to anon using (status = 'approved');

-- ---------- functions ----------
create or replace function hunt_check(p_pin text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not exists (select 1 from hunt_secret where pin = p_pin) then
    raise exception 'Wrong PIN';
  end if;
end $$;
revoke execute on function hunt_check(text) from public, anon, authenticated;

-- Student: record a submission (image already uploaded) and return their place in line.
create or replace function hunt_submit(p_round bigint, p_name text, p_path text) returns int
language plpgsql security definer set search_path = public as $$
declare v_pos int;
begin
  if not exists (
    select 1 from hunt_rounds
    where id = p_round and open
      and (seconds is null or now() < started_at + make_interval(secs => seconds + 5))
  ) then
    raise exception 'This round is closed';
  end if;
  if p_path !~ ('^' || p_round || '/[0-9a-f-]{36}\.jpg$') then
    raise exception 'Bad upload path';
  end if;
  insert into hunt_submissions (round_id, name, path) values (p_round, trim(p_name), p_path);
  select count(*) into v_pos from hunt_submissions where round_id = p_round;
  return v_pos;
end $$;

-- Public: how many screenshots have come in this round (for the projector).
create or replace function hunt_count(p_round bigint) returns int
language sql security definer set search_path = public as $$
  select count(*)::int from hunt_submissions where round_id = p_round;
$$;

-- Host-only (PIN-checked) functions.
create or replace function hunt_login(p_pin text) returns boolean
language plpgsql security definer set search_path = public as $$
begin perform hunt_check(p_pin); return true; end $$;

create or replace function hunt_new_round(p_pin text, p_prompt text, p_seconds int) returns bigint
language plpgsql security definer set search_path = public as $$
declare v_id bigint;
begin
  perform hunt_check(p_pin);
  update hunt_rounds set open = false where open;
  insert into hunt_rounds (prompt, seconds) values (p_prompt, p_seconds) returning id into v_id;
  return v_id;
end $$;

create or replace function hunt_close_round(p_pin text, p_round bigint) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform hunt_check(p_pin);
  update hunt_rounds set open = false where id = p_round;
end $$;

create or replace function hunt_list(p_pin text, p_round bigint) returns setof hunt_submissions
language plpgsql security definer set search_path = public as $$
begin
  perform hunt_check(p_pin);
  return query select * from hunt_submissions where round_id = p_round order by created_at;
end $$;

create or replace function hunt_set_status(p_pin text, p_id bigint, p_status text) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform hunt_check(p_pin);
  update hunt_submissions set status = p_status where id = p_id;
end $$;

grant execute on function hunt_submit(bigint, text, text), hunt_count(bigint),
  hunt_login(text), hunt_new_round(text, text, int), hunt_close_round(text, bigint),
  hunt_list(text, bigint), hunt_set_status(text, bigint, text) to anon;

-- ---------- image storage ----------
-- Public bucket = images load by URL (names are random UUIDs; the bucket can't be listed).
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('hunt', 'hunt', true, 5242880, array['image/jpeg'])
on conflict (id) do nothing;

drop policy if exists "hunt upload" on storage.objects;
create policy "hunt upload" on storage.objects for insert to anon
  with check (bucket_id = 'hunt');

-- ---------- host PIN ----------
-- Change this to something only you know (a short passphrase beats 4 digits). Re-run just
-- these two lines any time to change it.
delete from hunt_secret;
insert into hunt_secret (pin) values ('CHANGE-ME');
