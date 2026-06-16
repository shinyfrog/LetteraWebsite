#!/usr/bin/env python3
"""Extract design tokens from a .sketch file or .sketchpalette — no Sketch app needed.

A .sketch file is just a ZIP of JSON. This unzips it, walks the layer tree of one
page, and reports every text style, fill colour, border, corner radius and shadow,
ranked by how often each value is used. Frequency matters: the *dominant* value for a
role (e.g. the accent colour used 7x) is the real token; one-off values are usually
decoration or leftovers.

Usage:
  sketch_extract.py FILE.sketch                # default page (currentPageIndex)
  sketch_extract.py FILE.sketch --page Final   # a page by name
  sketch_extract.py FILE.sketch --list-pages   # just list page names
  sketch_extract.py FILE.sketchpalette         # palette -> hex list

Stdlib only. Output is Markdown on stdout.
"""
import argparse
import json
import sys
import zipfile
from collections import Counter


def hexof(c):
    return "#%02X%02X%02X" % (
        round(c.get("red", 0) * 255),
        round(c.get("green", 0) * 255),
        round(c.get("blue", 0) * 255),
    )


def extract_palette(path):
    with open(path) as f:
        data = json.load(f)
    print("# Sketch palette\n")
    seen = set()
    for c in data.get("colors", []):
        hx = hexof(c)
        a = round(c.get("alpha", 1), 2)
        key = (hx, a)
        if key in seen:
            continue
        seen.add(key)
        name = c.get("name") or ""
        print(f"- `{hx}`  alpha={a}  {name}".rstrip())


def read_zip_json(zf, name):
    with zf.open(name) as f:
        return json.load(f)


def walk(node, fonts, fills, borders, radii, shadows):
    if isinstance(node, dict):
        if node.get("_class") == "text":
            for run in node.get("attributedString", {}).get("attributes", []):
                at = run.get("attributes", {})
                fnt = at.get("MSAttributedStringFontAttribute", {}).get("attributes", {})
                col = at.get("MSAttributedStringColorAttribute")
                para = at.get("paragraphStyle", {}) or {}
                fam, sz = fnt.get("name"), fnt.get("size")
                lh = para.get("maximumLineHeight") or para.get("minimumLineHeight")
                if fam:
                    fonts[(
                        fam,
                        round(sz, 1) if sz else 0,
                        hexof(col) if col else "",
                        round(lh, 1) if lh else 0,
                    )] += 1
        style = node.get("style") if isinstance(node.get("style"), dict) else {}
        for fl in style.get("fills", []) or []:
            if fl.get("isEnabled") and fl.get("color"):
                fills[(hexof(fl["color"]), round(fl["color"].get("alpha", 1), 2))] += 1
        for b in style.get("borders", []) or []:
            if b.get("isEnabled") and b.get("color"):
                borders[(hexof(b["color"]), b.get("thickness", 0))] += 1
        for sh in style.get("shadows", []) or []:
            if sh.get("isEnabled") and sh.get("color"):
                c = sh["color"]
                shadows[(
                    hexof(c), round(c.get("alpha", 1), 2),
                    sh.get("offsetX"), sh.get("offsetY"),
                    sh.get("blurRadius"), sh.get("spread"),
                )] += 1
        r = node.get("fixedRadius") or node.get("cornerRadius")
        if r:
            radii[round(r, 2)] += 1
        for p in node.get("points", []) or []:
            cr = p.get("cornerRadius")
            if cr:
                radii[round(cr, 2)] += 1
        for v in node.values():
            walk(v, fonts, fills, borders, radii, shadows)
    elif isinstance(node, list):
        for v in node:
            walk(v, fonts, fills, borders, radii, shadows)


def extract_sketch(path, page_name, list_pages):
    with zipfile.ZipFile(path) as zf:
        meta = read_zip_json(zf, "meta.json")
        doc = read_zip_json(zf, "document.json")
        pages_meta = meta.get("pagesAndArtboards", {})
        names = {pid: v.get("name", pid) for pid, v in pages_meta.items()}

        if list_pages:
            print("# Pages\n")
            for pid, name in names.items():
                print(f"- {name}  ({pid})")
            return

        # Resolve the target page id.
        page_id = None
        if page_name:
            for pid, name in names.items():
                if name == page_name:
                    page_id = pid
                    break
            if not page_id:
                sys.exit(f"No page named {page_name!r}. Pages: {list(names.values())}")
        else:
            idx = doc.get("currentPageIndex", 0)
            refs = doc.get("pages", [])
            if refs and idx < len(refs):
                page_id = refs[idx]["_ref"].split("/")[-1]
            else:
                page_id = next(iter(names))

        page = read_zip_json(zf, f"pages/{page_id}.json")

    fonts, fills, borders, radii, shadows = Counter(), Counter(), Counter(), Counter(), Counter()
    walk(page, fonts, fills, borders, radii, shadows)

    print(f"# Tokens — page '{names.get(page_id, page_id)}'\n")
    print(
        "> Ranked by usage. The dominant value for each role is usually the real token; "
        "one-offs are often decoration or leftovers. Fonts that aren't the site's brand "
        "family (e.g. an app's own UI font, mono/math fonts) typically live *inside* "
        "screenshot mockups, not page chrome — judge by family name.\n"
    )

    print("## Text styles — family / size / colour / line-height : count\n")
    for (fam, sz, col, lh), n in fonts.most_common():
        print(f"- {n:3d}x  `{fam}`  size={sz}  colour={col}  lh={lh}")

    print("\n## Fill colours : count\n")
    for (hx, a), n in fills.most_common():
        print(f"- {n:3d}x  `{hx}`  alpha={a}")

    print("\n## Borders — colour / thickness : count\n")
    for (hx, t), n in borders.most_common():
        print(f"- {n:3d}x  `{hx}`  t={t}")

    print("\n## Corner radii : count\n")
    for r, n in radii.most_common():
        print(f"- {n:3d}x  {r}px")

    print("\n## Shadows : count\n")
    for (hx, a, x, y, blur, spread), n in shadows.most_common():
        print(f"- {n:3d}x  `{hx}` alpha={a}  x={x} y={y} blur={blur} spread={spread}")


def main():
    ap = argparse.ArgumentParser(description="Extract design tokens from a .sketch / .sketchpalette file.")
    ap.add_argument("file", help="path to a .sketch or .sketchpalette file")
    ap.add_argument("--page", help="page name to extract (default: the document's current page)")
    ap.add_argument("--list-pages", action="store_true", help="list page names and exit")
    args = ap.parse_args()

    if args.file.endswith(".sketchpalette"):
        extract_palette(args.file)
    else:
        extract_sketch(args.file, args.page, args.list_pages)


if __name__ == "__main__":
    main()
