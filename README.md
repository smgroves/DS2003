# DS 2003: Communicating with Data — course site

Static site for DS 2003, published via GitHub Pages at
**https://smgroves.github.io/DS2003/**

**This folder (`F26_DS2003_02/`) is the git repo.** There's no separate copy anywhere —
edit a lecture, lab, or activity here and it's editing the live site's source directly.
Commit + push to publish.

## Structure

- `index.html` — the schedule (lecture/activity/lab/reading/deadline per class day), the
  landing page Pages serves at the URL above
- `Lectures/` — lecture slides (`.pptx`), linked from the schedule where they exist
- `Labs/` — student-facing lab notebooks (`.ipynb`)
- `Class activities/` — in-class activities, e.g. `Subway_Map_Wayfinding_Activity.html`
  (Getting Around NYC) with its `maps/` images
- `Readings/` — assigned readings
- `Project 1/` — the exploratory analysis project assignment + rubric
- `Private/` — **never committed** (see `.gitignore`) — anything with student PII or other
  non-public info goes here, e.g. the majors/minors roster

## What's deliberately excluded from the public repo (see `.gitignore`)

- `Private/` — student rosters, grades, anything with PII
- `*_filled_*.ipynb` — instructor answer-key notebooks (e.g. `Lab0_filled_python.ipynb`);
  only the `_blank_` student versions are published
- Quiz and exit-ticket *content* is intentionally never written into `index.html` — only
  the fact that one happens that day is shown

If you add a new lab, always keep the answer-key copy named with `_filled_` in the
filename so it's auto-excluded.

No build step, no Jekyll (`.nojekyll` disables it as a backstop) — just plain HTML/CSS,
served as-is, with real `.pptx`/`.ipynb`/`.pdf` files linked directly (they download or
open in whatever app/extension the visitor has — there's no in-browser preview for these
file types on a plain static site).

## Deploying

```bash
# one-time setup (already done for this repo):
gh repo create smgroves/DS2003 --public --source=. --remote=origin
git push -u origin main
```

Then in the repo's **Settings → Pages**: Source = **Deploy from a branch**, Branch = **main**,
folder = **/ (root)**. Live in a minute at the URL above.

## Updating

Edit anything in this folder, `git add`, commit, push — Pages rebuilds automatically on
every push to `main`. Since this folder also lives in Box, Box will keep syncing your
edits across your devices as always; only `git push` actually publishes them.
