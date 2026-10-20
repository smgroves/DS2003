# Screenshot Hunt

A live in-class game: you put up a prompt ("Find an example of *selection* interactivity in
an app on your phone"), students race to screenshot one and send it from their phone, and
you put the best ones on the projector.

| Page | Who | URL |
|---|---|---|
| `index.html` | Students (phones) | https://smgroves.github.io/DS2003/hunt/ |
| `screen.html` | The projector | https://smgroves.github.io/DS2003/hunt/screen.html |
| `control.html` | You (laptop or phone), PIN-locked | https://smgroves.github.io/DS2003/hunt/control.html |

## One-time setup (~10 minutes)

1. Make a free project at [supabase.com](https://supabase.com) (any name and region).
2. In the project, open **SQL Editor**, paste all of `setup.sql`, **change `CHANGE-ME` on the
   last line to your own PIN/passphrase**, and click **Run**.
3. Open **Project Settings → API** (or **API Keys**) and copy the **Project URL** and the
   **anon / publishable** key into `config.js`. (That key is designed to be public, so it's
   fine in this public repo. The PIN stays in the database, never in the repo.)
4. Commit and push. The pages go live with the rest of the site.

## In class

1. Open `screen.html` on the projector. Before the first round it shows a big QR code.
   Students scan it once, type their name, and **keep that tab open** all class.
2. Open `control.html` somewhere students can't see: your phone, or a laptop window
   that isn't mirrored to the projector. Pick a prompt, set a time limit, and **Start round**.
3. Each round, students take a screenshot, switch back to the tab, tap **Send screenshot**,
   and pick it. Their phone tells them their place in line ("#3").
4. Submissions show up on `control.html` in arrival order with a time (+12.4s). Tap a
   thumbnail to enlarge it, then **Show** to put it on the projector. The earliest shown
   one gets the gold #1 badge. **Hide** keeps it off the screen.

Nothing goes on the projector until you tap **Show**.

## Notes

- Edit `prompts.js` to change the ready-made prompts.
- Images are shrunk on the phone (≤1600px JPEG) before upload, so sends are quick.
- Uploaded images live in the Supabase `hunt` storage bucket under random file names.
  Anyone with an exact image link could open it, but the bucket can't be browsed or listed.
  To clear old games, delete files in **Storage → hunt** and rows in **Table Editor →
  hunt_submissions / hunt_rounds**.
- To change the PIN, re-run the last two lines of `setup.sql` with a new value.
