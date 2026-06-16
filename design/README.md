# Design source

Committed, diffable design artifacts for the Lettera website.

| File | What it is |
|---|---|
| `DESIGN.md` | The design system — canonical tokens + a conformance audit of the live code. **Start here.** |
| `preview.png` | Exported render of the Sketch "Final" page (the visual target). |
| `lettera.sketchpalette` | Brand/app-icon colour swatches (reds). Note: these are *not* the website-chrome colours — the site is blue-accented. |

## Source of truth

The editable `Lettera Website - Beta Release.sketch` (~14 MB binary) is **not** committed
— it's gitignored to keep history lean and out of the GitHub Pages deploy. It lives in the
shared drive. When the design changes, re-export `preview.png` and update `DESIGN.md`.

A `.sketch` file is a ZIP of JSON, so it can be inspected without the Sketch app:

```sh
unzip -d /tmp/sketch "Lettera Website - Beta Release.sketch"
# then read /tmp/sketch/pages/*.json, document.json, meta.json
```
