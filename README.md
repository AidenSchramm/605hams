# 605hams.com — 605 Ham Map

Interactive map of South Dakota amateur radio clubs and linked repeater systems
(SD-LINK, Prairie Dog ARC, Northern Hills), hosted on GitHub Pages.

## How it works

- `index.html` — the whole app: basemap, markers, panel, zoom/pan. No build step,
  no dependencies, no tile server.
- `data.json` — all club, site, repeater and link data. **This is the source of truth.**
- `logos/` — club logos (WebP).
- `photos/` — site photos (WebP), referenced from each site's `photos[]`.
- `qr-605hams.png` / `.svg` — QR code for https://605hams.com/, for business cards and
  flyers. Error-correction level H, so it still scans with a logo over the middle or a
  trimmed edge. The SVG is vector — use that for print.
- `CNAME` — custom domain for GitHub Pages.

The site is read-only — visitors browse, zoom, pan, and click markers. Repeater
sites that sit on top of each other at the current zoom merge into a numbered
cluster; clicking it lists every repeater at that location.

The basemap is real geometry (state boundary, county lines, the Missouri/Cheyenne/
James rivers, Lake Oahe and Lake Francis Case, I-90 and I-29), simplified and
inlined as encoded polylines in `index.html`.

Marker and label sizes are the constants `R_SITE`, `R_CLUSTER`, `R_CLUB`, `LBL`,
`CITY` and `MERGE` near the top of the render code — raise them to make everything
bigger, lower `MERGE` to make nearby sites stop grouping so eagerly.

## Updating the data

1. Edit `data.json` (the pencil icon on github.com works fine).
2. Run `python3 tools/sync_seed.py` to copy it into the inline fallback in
   `index.html`, and commit both files.

GitHub Pages redeploys about a minute later.

Step 2 matters: `index.html` carries an inline copy of `data.json` so the page
still renders when the fetch fails (file:// preview, offline). If you skip it the
live site is still correct — it fetches `data.json` — but the fallback goes stale.

### Structure

- `clubs` — name, callsign, city, lat/lon, address, meeting, mailing, website,
  discord, logo.
- `sites` — name, `system` (`sdlink` / `pdarc` / `nh` / `none`), lat/lon, notes,
  photos, and `repeaters[]`.
- `repeaters[]` — label, type, `out` (output, what you listen on), `in` (input,
  what you transmit on), tone, optional `owner` callsign and `note`. A site can
  host repeaters owned by different clubs. **Backbone link pairs are deliberately
  not listed** — publishing them invites people to key up on the link.
- `links` — pairs of site ids plus the system, drawn as the colored RF-link lines.
- `discord.url` — the statewide Discord button in the nav (hidden while empty).
- `resources` — the "Elsewhere in South Dakota radio" list on the landing panel.
  Groups of `{label, url, note}`; add or reorder freely, the panel follows.
