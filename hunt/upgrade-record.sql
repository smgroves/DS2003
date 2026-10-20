-- Screenshot Hunt: "best picks" + saved record of past rounds.
-- Run once in Supabase → SQL Editor (New query → paste → Run), after setup.sql.
-- Safe to re-run. Does not touch your PIN.

alter table hunt_rounds      add column if not exists saved      boolean not null default false;
alter table hunt_rounds      add column if not exists show_names boolean not null default false;
alter table hunt_submissions add column if not exists starred    boolean not null default false;

-- Hiding a submission also un-stars it.
create or replace function hunt_set_status(p_pin text, p_id bigint, p_status text) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform hunt_check(p_pin);
  update hunt_submissions set status = p_status, starred = starred and p_status <> 'rejected'
  where id = p_id;
end $$;

-- Starring a submission also shows it on the projector.
create or replace function hunt_set_star(p_pin text, p_id bigint, p_star boolean) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform hunt_check(p_pin);
  update hunt_submissions
  set starred = p_star, status = case when p_star then 'approved' else status end
  where id = p_id;
end $$;

-- Add a round to (or remove it from) the public record.
create or replace function hunt_save_round(p_pin text, p_round bigint, p_saved boolean, p_show_names boolean)
returns void language plpgsql security definer set search_path = public as $$
begin
  perform hunt_check(p_pin);
  update hunt_rounds set saved = p_saved, show_names = p_show_names where id = p_round;
end $$;

-- Public record: saved rounds with every submission except hidden ones.
-- Names are included only for rounds saved with "show names" ticked.
drop function if exists hunt_archive();
create function hunt_archive()
returns table (round_id bigint, prompt text, started_at timestamptz,
               sub_id bigint, name text, path text, starred boolean, created_at timestamptz)
language sql security definer set search_path = public as $$
  select r.id, r.prompt, r.started_at,
         s.id, case when r.show_names then s.name end, s.path, s.starred, s.created_at
  from hunt_rounds r
  left join hunt_submissions s on s.round_id = r.id and s.status <> 'rejected'
  where r.saved
  order by r.id desc, s.created_at;
$$;

grant execute on function hunt_set_star(text, bigint, boolean),
  hunt_save_round(text, bigint, boolean, boolean), hunt_archive() to anon;
