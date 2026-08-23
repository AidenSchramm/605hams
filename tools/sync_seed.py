#!/usr/bin/env python3
"""Copy data.json into the <script id="seed"> fallback inside index.html.

data.json is the source of truth. index.html carries an inline copy so the page
still renders when data.json cannot be fetched (file:// preview, artifact viewer).
Run this after editing data.json:

    python3 tools/sync_seed.py
"""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
seed = json.dumps(json.loads((root / "data.json").read_text(encoding="utf-8")),
                  ensure_ascii=False, separators=(",", ":"))
if "</script" in seed.lower():
    sys.exit("data.json contains a </script> sequence; refusing to inline it.")

path = root / "index.html"
html = path.read_text(encoding="utf-8")
pat = re.compile(r'(<script type="application/json" id="seed">)(.*?)(</script>)', re.S)
m = pat.search(html)
if not m:
    sys.exit('No <script id="seed"> block found in index.html.')
if m.group(2) == seed:
    print("seed already up to date")
else:
    path.write_text(html[:m.start(2)] + seed + html[m.end(2):], encoding="utf-8")
    print(f"seed updated ({len(seed)} bytes)")
