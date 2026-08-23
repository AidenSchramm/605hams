# 605hams.com — 605 Ham Map

Interactive map of South Dakota amateur radio clubs and linked repeater systems
(SD-LINK, Prairie Dog ARC, Black Hills), hosted on GitHub Pages.

## How it works

- `index.html` — the whole app (map, popups, zoom/pan). No build step.
- `data.json` — all club/repeater/link data. The page loads this at startup.
- `CNAME` — custom domain for GitHub Pages.

The site is **read-only** — visitors can browse, zoom, pan, and click markers.
Repeater sites that sit on top of each other at the current zoom merge into a
numbered cluster node; clicking it lists every repeater at that location.

## Updating the data

Edit `data.json` in this repo (the pencil icon on github.com works fine) and
commit — the site picks up the change when GitHub Pages redeploys, about a
minute later.

Structure: `clubs` (name, callsign, city, lat/lon, meeting, mailing, website,
discord, repeaters, notes), `sites` (name, system: `sdlink`/`pdarc`/`bh`
(= Northern Hills linked system, historical key)/`none`,
lat/lon, notes, photos, repeaters[]), and `links` (pairs of site ids with a
system). The top-level `discord.url` populates the nav-bar Discord button
(hidden while empty).
