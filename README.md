# 605hams.com — SoDak Ham Map

Interactive map of South Dakota amateur radio clubs and linked repeater systems
(SD-LINK, Prairie Dog ARC, Black Hills), hosted on GitHub Pages.

## How it works

- `index.html` — the whole app (map, popups, edit mode). No build step.
- `data.json` — all club/repeater/link data. The page loads this at startup.
- `CNAME` — custom domain for GitHub Pages.

## Editing

Anyone can view. To edit, open the site, click **✎ Edit**, make changes, and hit
**Save changes**. Saving commits `data.json` back to this repo through the GitHub
API, which requires a token pasted once into the Edit toolbar (stored only in
that browser):

1. GitHub → Settings → Developer settings → **Fine-grained personal access tokens**
2. New token, scoped to **only this repository**, with **Contents: Read and write**
3. Paste it into the "GitHub token" field in the site's Edit toolbar

Edits go live when GitHub Pages redeploys (about a minute after saving).

You can also just edit `data.json` directly in the repo — the site renders
whatever is committed.
