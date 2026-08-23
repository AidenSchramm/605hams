# 605hams.com — 605 Ham Map

Interactive map of South Dakota amateur radio clubs and linked repeater systems
(SD-LINK, Prairie Dog ARC, Black Hills), hosted on GitHub Pages.

## How it works

- `index.html` — the whole app (map, popups, zoom/pan). No build step.
- `data.json` — all club/repeater/link data. The page loads this at startup.
- `CNAME` — custom domain for GitHub Pages.

The public site is **read-only** — visitors can browse, zoom, and click markers,
but there is no editing UI on the live site.

## Updating the data

Edit `data.json` in this repo (the pencil icon on github.com works fine) and
commit — the site picks up the change when GitHub Pages redeploys, about a
minute later.

Structure: `clubs` (name, callsign, city, lat/lon, meeting, mailing, website,
repeaters, notes), `sites` (name, system: `sdlink`/`pdarc`/`bh`/`none`, lat/lon,
notes, photos, repeaters[]), and `links` (pairs of site ids with a system).

For visual editing (drag markers, forms, photo upload), open the site from
`http://localhost` — the edit UI appears in development only. Preview changes
locally, then copy the resulting data into `data.json`.
