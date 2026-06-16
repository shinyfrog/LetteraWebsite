---
name: sketch-design-tokens
description: >-
  Extract a design system (colours, type styles, corner radii, shadows, borders) from a
  Sketch file — `.sketch` or `.sketchpalette` — without needing the Sketch app installed.
  Use this whenever a designer hands over a `.sketch`/`.sketchpalette` and you need the
  real tokens: "what are the brand colours / fonts in this Sketch file", "pull the type
  scale out of the design", "extract the palette", "I don't have Sketch but need the
  values", or any time you must reconcile shipped CSS against a Sketch source of truth.
  Reach for it even if the user just attaches a `.sketch` and asks what's in it.
---

# Sketch design tokens

A `.sketch` file is a ZIP of JSON, and a `.sketchpalette` is a plain JSON colour array —
so the design system can be read precisely **without the Sketch app**. The bundled script
does the parsing; this guide is about turning its raw output into a trustworthy token set.

## Extract

```bash
python3 scripts/sketch_extract.py "path/to/Design.sketch" --list-pages   # see page names
python3 scripts/sketch_extract.py "path/to/Design.sketch" --page Final   # tokens for a page
python3 scripts/sketch_extract.py "path/to/palette.sketchpalette"        # palette -> hex
```

Stdlib-only, output is Markdown. A `.sketch` usually has several pages (e.g. a current
design plus older drafts) — list them first and pick the finished one rather than guessing.

## Reading the output — the part that matters

The script ranks every value by **usage count**. That ranking is the whole point:

- **The dominant value for a role is the real token.** When two similar blues both appear,
  the one used 7× is the accent; the one used 3× is a decoy or a one-off. Don't pick by eye
  or by which looks "nicer" — pick by frequency, then sanity-check visually.
- **Separate page chrome from screenshot-baked styles.** Marketing pages embed product
  screenshots, and those screenshots contain their *own* fonts and colours (an app's UI
  font, mono fonts for code, math fonts, 5%-alpha code-chip tints). Those are baked into
  raster PNGs and must **not** become website CSS tokens. Tell them apart by family: the
  site's brand font (here, the headings/body family) is chrome; everything else is usually
  inside a mockup. Call this split out explicitly when you report tokens.
- **A companion `.sketchpalette` is often not the website palette.** Palettes frequently
  hold brand/app-icon swatches (e.g. logo reds) that never appear in the web chrome. Verify
  against the page's actual fill colours before treating palette entries as site tokens.
- **One-offs are suspects, not tokens.** A radius or colour that appears once is more likely
  decoration, a single accent corner, or a leftover than a systematic value.

## Turning tokens into CSS custom properties

Group the dominant values into a small, named set — backgrounds/surfaces, ink/text,
accent, lines, radii, shadows. Note that Sketch colour objects are 0–1 RGBA, so the script
already converts to hex. Sketch shadow colours are frequently a cool grey rather than pure
black — preserve the actual tint rather than defaulting to `rgba(0,0,0,…)`.

For the deeper structure of the JSON (where to find more than the script surfaces — symbols,
shared styles, artboard frames), see `references/sketch-json-format.md`.
