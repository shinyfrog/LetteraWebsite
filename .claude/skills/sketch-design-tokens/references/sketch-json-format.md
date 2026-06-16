# Sketch file format (for deeper extraction)

A `.sketch` file is a ZIP archive. Unzip it (`unzip -d out file.sketch`) to get:

```
document.json     top-level: currentPageIndex, pages[] (refs), assets, sharedSwatches,
                  layerStyles, layerTextStyles, foreign* libraries
meta.json         pagesAndArtboards{} keyed by page UUID -> { name, artboards }; app version
pages/<uuid>.json one file per page; the layer tree lives here
images/           bitmaps referenced by layers (hashed filenames)
fonts/            embedded font binaries (hashed filenames)
previews/preview.png   a rendered thumbnail of the document — handy as a visual target
```

## Layer tree

Each page JSON has a `layers[]` array; layers nest via their own `layers[]`. Every node
has a `_class` (`artboard`, `group`, `text`, `rectangle`, `bitmap`, `shapePath`, …) and a
`frame` (`{x, y, width, height}`). The extractor script recurses the whole tree.

## Where the values live

- **Colours** are objects with `red`/`green`/`blue`/`alpha` in the **0–1** range (not 0–255).
- **Text styles**: `node.attributedString.attributes[].attributes` →
  `MSAttributedStringFontAttribute.attributes` (`name`, `size`),
  `MSAttributedStringColorAttribute` (a colour object), and `paragraphStyle`
  (`maximumLineHeight` / `minimumLineHeight`, alignment). `kerning` sits alongside.
- **Fills / borders / shadows**: `node.style.fills[]`, `node.style.borders[]`,
  `node.style.shadows[]`. Each has `isEnabled` (skip disabled ones) and a `color`. Borders
  add `thickness`; shadows add `offsetX/offsetY/blurRadius/spread`.
- **Corner radii**: `fixedRadius` on rectangles, or per-point `cornerRadius` inside
  `node.points[]` for custom shapes.

## Shared / reusable styles (often empty)

`document.json` may define `layerTextStyles.objects[]` and `layerStyles.objects[]` (named,
reusable styles) and `sharedSwatches.objects[]` (named colours). Designers don't always use
them — in many files these are empty and the real styling is inline on each layer, which is
why the script harvests inline values and ranks by frequency instead of trusting shared
styles. When shared styles *are* populated, they're the cleanest source of canonical tokens.
