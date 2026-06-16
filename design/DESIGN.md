# Lettera Website — Design System

The single reference for the Lettera marketing site's visual language. Tokens here are
the **canonical target**, reconciled from the Sketch source against usage frequency. Where
the shipped CSS disagrees, this file states the target and the
[Conformance audit](#conformance-audit) lists the deviation.

## Source of truth

- **File:** `Lettera Website - Beta Release.sketch` → page **"Final"**
  (the page named "Final"; "Previous version (without final blue)" is superseded).
- **Canvas width:** **1200 px** (artboard "Homepage - Blue Color Final", 1200×6377).
- **Companion palette:** `untitled.sketchpalette` — a **brand/app-icon** red swatch set
  (`#C31A1E … #E6152D`, greys). These are **not** website-chrome colors; the site is
  blue-accented. Do not pull website tokens from this palette.
- A `.sketch` file is a ZIP of JSON. To re-inspect without the app:
  `unzip -d out file.sketch` → read `pages/*.json`, `document.json`, `meta.json`.

### Two font/colour domains — keep them separate

Roughly half the type/colour in the Sketch file lives **inside the editor screenshot
mockups** (BearSansUI, SF Mono, Roboto Mono, MathJax; greens/purples/code tints). Those
ship as **raster PNGs** in `assets/`, never as live page text. Only the **Plus Jakarta
Sans** page chrome belongs in CSS. This document covers page chrome; mockup styling is
baked into the images.

---

## Colour

Canonical website-chrome tokens. Hex values are the dominant Sketch value for each role.

### Backgrounds & surfaces

| Token | Value | Role |
|---|---|---|
| `--bg` | `#FFFFFF` | Page background, cards, inputs (33× in source) |
| `--surface` | `#F3F5F7` | Section bands, showcase / know / more cards (16× — the dominant band colour) |
| `--surface-2` | `#F1F4F6` | Secondary band tint (8×) — use only if a second tier is needed |
| `--footer-bg` | `#141313` | Dark footer. ⚠️ Only near-black fill in the source; **confirm with designer** |

### Text / ink

| Token | Value | Role |
|---|---|---|
| `--ink-hero` | `#000000` | Hero wordmark **only** (pure black, distinct from `--ink`) |
| `--ink` | `#242629` | All section & card headings |
| `--ink-soft` | `#444444` | Long-form body text (mostly mockup content) |
| `--muted` | `#718AA2` | Section subtitles, nav links |
| `--muted-2` | `#7E94AA` | Card body copy |
| `--caption` | `#888888` | Captions / fine print |

### Accent & highlights

| Token | Value | Role |
|---|---|---|
| `--accent` | `#1874D3` | **Primary blue** — buttons, links, focus ring (7× — dominant) |
| `--accent-bright` | `#226CF7` | Brighter blue, secondary emphasis / inline links (3×) |
| `--accent-hover` | `#1568BE` | Darker accent for button hover |
| `--hl-green` | `#DBFDAE` | Green text highlight (`<mark>`) |
| `--hl-purple` | `#F8DCFD` | Purple text highlight (`<mark>`) |

### Lines, borders & semantic states

| Token | Value | Role |
|---|---|---|
| `--line` | `#D9D9D9` | Hairline borders / dividers (source chrome border, t=1) |
| `--success` | `#1D7D3F` | Form success message |
| `--error` | `#D9382F` | Form error message |

> macOS traffic-light dots (`#FF5F57 / #FEBC2E / #28C840`) and the 5%-alpha code-chip
> tints are mockup decoration, intentionally **not** tokens.

### Shadows

Source shadows are tinted **cool blue-grey `#717F8C`**, not ink.

| Token | Value | Role |
|---|---|---|
| `--shadow-card` | `0 0 20px rgba(113,127,140,.06)` | Soft card glow (6× in source) |
| `--shadow-float` | `4px 4px 30px rgba(113,127,140,.25)` | Floating element |
| `--shadow-mock` | `0 20px 50px rgba(113,127,140,.14)` | Screenshot/mockup drop shadow |
| hero icon | `0 0 60px rgba(0,0,0,.15)` | Hero app-icon glow (blur 60 in source) |

---

## Typography

**Family:** `"Plus Jakarta Sans"`, system fallback. Loaded via Google Fonts
(`index.html:13–15`, weights 400/500/600/700/800 + italic-500, `display=swap`). ✅ Loaded.

Letter-spacing: the Sketch source carries **no kerning** on chrome text — any negative
`letter-spacing` in CSS is a stylistic add, not from the design.

### Type scale (page chrome)

| Role | Weight | Size | Line-height | Colour |
|---|---|---|---|---|
| Hero wordmark | 700 | 72 px / 4.5rem | 1.0 | `--ink-hero` |
| Section H2 | 700 | 46 px / 2.875rem | ~1.1 | `--ink` |
| Display (alt) | 700 | 40 px / 2.5rem | ~1.1 | `--ink` |
| Card / sub heading | 700 (or 600) | 30 px / 1.875rem | 1.2 | `--ink` |
| Button label (primary) | 600 | 20 px / 1.25rem | 1.0 | `#FFFFFF` |
| Section subtitle | 500 | 24 px / 1.5rem | 40 px (≈1.67) | `--muted` |
| Section subtitle (lg) | 500 | 28 px / 1.75rem | ~1.4 | `--muted` |
| Card / body copy | 500 | 18 px / 1.125rem | 28–30 px (≈1.6) | `--muted-2` |
| Inline link | 500 | 18 px / 1.125rem | 30 px | `--accent-bright` |
| Button label (small) | 500 | 16 px / 1rem | 1.0 | `#FFFFFF` |
| Caption | 500 | 16 px / 1rem | 1.4 | `--caption` |

### Mockup-only fonts (do **not** map to CSS)

Inside the screenshot PNGs only: **BearSansUI** (Lettera's UI font, 13–34 px),
**SF Mono** 8 px, **Roboto Mono** 20 px, **MathJax** 18/26 px, **SF Pro** 10–24 px.

---

## Spacing

The site uses a loose 4/8-based ramp. Recommended canonical scale (introduce as
`--space-*` tokens; current CSS hard-codes every value):

`4 · 8 · 12 · 16 · 20 · 24 · 28 · 32 · 40 · 48 · 56 · 64`

Section vertical rhythm: **84 px** desktop (`--space-section`), **64 px** ≤900 px.
Off-grid values in the current CSS to normalise: `84` (→ 80/88), `52`, `38`, `30`.

---

## Radii

| Token | Value | Usage |
|---|---|---|
| `--radius-lg` | 32 px | Large containers, footer top corners (32× in source) |
| `--radius-md` | 18 px | Cards (96× — the dominant card radius) |
| `--radius-sm` | 10 px | Buttons, inputs (source small radius is 10/6 px — **not** 12) |
| `--radius-shot` | 35 px | TOC screenshot top-right corner only (distinct from `--radius-lg`) |
| `--radius-pill` | 100 px | Pills / round affordances |

---

## Layout & responsive

- **Container:** `--container: 1160px` + `24px` inline padding = 1208 px outer, ≈20 px
  gutters inside the 1200 px canvas. Correct — "canvas minus gutter". Narrow variant
  `760px` for FAQ / newsletter.
- **Breakpoints:** `900px` (bento & know-card stack), `760px` (nav, dual-grid, more-card
  stack), `560px` (mobile fine-tuning). Coherent ladder.
- **Reduced motion:** `prefers-reduced-motion` disables reveal/scroll animation. ✅

---

## Components

| Component | Spec |
|---|---|
| **Button** primary | `--accent` bg, white **20 px/600** label (`.btn-lg`), `--radius-sm`, accent glow shadow. Hover → `--accent-hover`. Needs `:focus-visible`. |
| **Button** small | white **16 px/500** label. |
| **Header / nav** | Sticky, translucent-white blur, 68 px row, brand mark + nav + CTA; `.scrolled` adds border+shadow. ⚠️ **Designed but not implemented** — see audit. |
| **Hero** | Wordmark "Letter" + app-icon standing in for the final "a" (rotated 14°, soft glow); tagline `--muted`; CTA; full-bleed screenshot fading into page. |
| **Showcase card** | `--surface`, `--radius-lg`, 40 px padding; mockup image 80 %-width, top-rounded, bottom fade into card. |
| **Bento card** | `#FFFFFF`, `--radius-md`, `--shadow-card`; image `object-fit:contain`. Top row 2:1, bottom row 1:2. |
| **Know card** | Split `--surface` card; TOC screenshot masked to a fixed height, top-right corner `--radius-shot`, fade-out; two text blocks. |
| **More card** | `--surface`, `--radius-lg`, 56 px padding; 2-col grid with centre divider; centre CTA. |
| **FAQ** | Native `<details>`, hairline divider, 30 px/600 summary, chevron indicator that rotates on `[open]`. |
| **Newsletter** | Email input (1.5 px border, accent focus ring) + primary button; `role=status` live message. |
| **Footer** | `--footer-bg` dark, `--radius-lg` top corners; brand + two `<nav>` columns + bottom bar. |

---

## Accessibility baseline

- Provide a single, consistent `:focus-visible` ring (`2px solid var(--accent)`,
  `outline-offset: 2px`) on `.btn`, links, and `summary`.
- **Contrast:** `--muted` / `--muted-2` on white are ≈3:1 — **below WCAG AA (4.5:1)** for
  body text. Reserve them for large text only, or darken for small copy. Footer whites at
  `.55`/`.66` alpha similarly fail; lift to ≥`.7`.
- Decorative images get `alt=""`; informative images get distinct, accurate alt text.
- A skip link + header landmark once the header is implemented.

---

## Conformance audit

Findings from a 5-track review of the shipped code against this system, prioritised.
File:line references are to `index.html` / `styles.css` / `script.js`.

### P0 — shipping bugs (functional breakage)

1. **Bento `srcset` 1× paths are doubled** → `assets/bento/assets/bento/…@1x.png`.
   Images break on non-retina displays. `index.html:90, 95, 103, 108, 113, 117`.
2. **`grid-template-columns: 2fr, 1fr` / `1fr, 2fr`** — commas are invalid in grid track
   lists; the declaration is dropped and the bento 2:1 / 1:2 ratios silently collapse.
   `styles.css:344, 351` → use `2fr 1fr` / `1fr 2fr`.
3. **Know-card image wrapper has no class** (`<div class="">`), so all `.know-visual`
   styling (height mask, 35 px corner, fade) is dead. `index.html:135`.
4. **Showcase image class mismatch** — markup uses `.showcase-visual`, CSS sizes
   `.showcase-visual--image img`, so the 80 %-width/radius/shadow never apply.
   `styles.css:303` vs `index.html:60, 71`.

### P1 — design-token deviations

5. `--accent: #226cf7` → **`#1874D3`** (dominant). Also update hard-coded copies
   `rgba(34,108,247,…)` at `styles.css:82, 501`. `styles.css:15`.
6. `--surface: #f1f4f6` → **`#F3F5F7`**. Also gradient stops at `styles.css:300, 416`.
   `styles.css:8`.
7. `--accent-d` equals `--accent`, so `.btn-primary:hover` is a no-op → set
   **`#1568BE`**. `styles.css:16, 84`.
8. `--footer-bg: #1f2227` is **not in the source** (marked "inferred") → `#141313`
   (verify). `styles.css:19`.
9. `--radius-sm: 12px` has no basis in the source (10/6 px) → **10 px**. `styles.css:23`.
10. `.hero-title: 4.75rem` (76 px) → **4.5rem (72 px)**; the `clamp()` is commented out
    (`styles.css:171`), so the hero can overflow on phones — restore fluid sizing.
11. Shadows are ink-tinted `rgba(36,38,41,…)`; source uses cool grey `#717F8C` —
    re-author `--shadow-card` / `--shadow-float` and the repeated mockup shadow.
    `styles.css:25, 26, 307, 316, 409`.

### P2 — structure, a11y, hygiene

12. **No header/nav exists** in `index.html` although the design (and ~70 lines of CSS:
    `.site-header`, `.nav`, `.nav-toggle`, `.mobile-menu`) call for a sticky header.
    Biggest structural gap: implement it or delete the dead CSS.
13. **No `:focus-visible`** anywhere except the newsletter input — keyboard users get no
    visible focus on buttons, links, or FAQ summaries.
14. **Muted-text contrast fails WCAG AA** (`--muted` / `--muted-2` ≈3:1 on white; footer
    `.55`/`.66` whites on dark).
15. **FAQ chevron never renders** — `[open] summary::after` rotates a pseudo-element whose
    base `::after` is undefined. `styles.css:469`.
16. **Duplicate / inaccurate `alt`** — hero and the "note" image share identical alt text;
    the note is not a state diagram. `index.html:40, 61`. Hero `<div>` is also illegally
    nested inside `<h1>` (`index.html:29`) — use a `<span>`.
17. **Dead CSS / refactor leftovers:** `.doc-mock` & friends, `.tips-table`/`kbd`/
    `.math-expr`, `.caret` (reduced-motion block), `.hero-shot-overlay`, the duplicated
    `grid-area` block (`styles.css:586–591`), the empty `.bento-card {}` (`styles.css:630`).
18. **Scroll-reveal system is inert** — `.reveal` styles exist but no element carries the
    class and `script.js` (newsletter only) never adds `.in`.
19. **Tokenise split magic values** — success `#1d7d3f` (CSS) vs error `#d9382f` (JS)
    should both be `--success`/`--error`; footer white alphas and accent-derived `rgba()`
    should derive from tokens.
