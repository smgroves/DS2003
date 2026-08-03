# DS 2003: Communicating with Data — course site

Static site for DS 2003, published via GitHub Pages at
**https://smgroves.github.io/DS2003/**

## Structure

- `index.html` — schedule + links to activities, lectures, readings (some link to Canvas, which is student-only)
- `getting-around-nyc/` — the subway map wayfinding activity (`index.html` + `maps/` images), live at `https://smgroves.github.io/DS2003/getting-around-nyc/`

No build step, no Jekyll (`.nojekyll` disables it as a backstop) — just plain HTML/CSS/JS,
served as-is. All links are relative so the site works unchanged at its `/DS2003/` subpath.

## Deploying

```bash
# one-time setup (already done for this repo):
gh repo create smgroves/DS2003 --public --source=. --remote=origin
git push -u origin main
```

Then in the repo's **Settings → Pages**: Source = **Deploy from a branch**, Branch = **main**,
folder = **/ (root)**. Live in a minute at the URL above.

## Updating

Edit, commit, push — Pages rebuilds automatically on every push to `main`.
