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

## Visual theme & atmosphere

**Calm, native-macOS premium.** The page feels like an Apple product page rendered through
a writing-app lens: airy, unhurried, and confident. Generous vertical breathing room
(84 px between sections) lets each idea land on its own. The reading column is centred and
narrow; nothing fights for attention.

- **Rhythm** — the page breathes by **alternating bands**: pure-white sections give way to
  soft cool-grey (`#F3F5F7`) bands, a quiet metronome that segments the story without rules
  or hard edges.
- **Light & material** — overwhelmingly light. Surfaces are paper-white and pale grey;
  depth comes from **whisper-soft, cool-grey diffused shadows**, never hard drop shadows.
  Cards feel like they rest a millimetre above the page, not float above it.
- **Shape language** — **softly rounded throughout.** Generously rounded containers
  (32 px) and comfortably rounded cards (18 px) set a friendly, tactile tone with no sharp
  corners anywhere in the chrome.
- **Colour temperament** — a near-monochrome canvas of cool greys and off-blacks, punctuated
  by a single **trustworthy editorial blue** (`#1874D3`) reserved for actions and links.
  Restraint is the point: one accent, used sparingly, reads as deliberate and calm.
- **Storytelling** — the page is **screenshot-led**. Real editor imagery, faded gently into
  its card at the bottom edge, carries the message; copy stays terse and supportive.
- **Voice in type** — large, tightly-set bold headings (Plus Jakarta Sans) over muted
  blue-grey body copy. The contrast of confident heading vs. soft secondary text is the
  core typographic gesture.

One-line brief: *a refined, light, blue-accented macOS landing page — calm whitespace,
soft-cornered cards, feather-light shadows, screenshots doing the talking.*

---

## Colour

Canonical website-chrome tokens. Hex values are the dominant Sketch value for each role.

### Backgrounds & surfaces

| Token | Character | Value | Role |
|---|---|---|---|
| `--bg` | Paper White | `#FFFFFF` | Page background, cards, inputs (33× in source) |
| `--surface` | Cool Mist Grey | `#F3F5F7` | Section bands, showcase / know / more cards (16× — the dominant band colour) |
| `--surface-2` | Faint Fog Grey | `#F1F4F6` | Secondary band tint (8×) — use only if a second tier is needed |
| `--footer-bg` | Near-Black Ink | `#141313` | Dark footer. ⚠️ Only near-black fill in the source; **confirm with designer** |

### Text / ink

| Token | Character | Value | Role |
|---|---|---|---|
| `--ink-hero` | True Black | `#000000` | Hero wordmark **only** (pure black, distinct from `--ink`) |
| `--ink` | Graphite Off-Black | `#242629` | All section & card headings |
| `--ink-soft` | Soft Charcoal | `#444444` | Long-form body text (mostly mockup content) |
| `--muted` | Slate Blue-Grey | `#718AA2` | Section subtitles, nav links |
| `--muted-2` | Pale Slate Blue | `#7E94AA` | Card body copy |
| `--caption` | Neutral Grey | `#888888` | Captions / fine print |

### Accent & highlights

| Token | Character | Value | Role |
|---|---|---|---|
| `--accent` | Editorial Blue | `#1874D3` | **Primary blue** — buttons, links, focus ring (7× — dominant) |
| `--accent-bright` | Vivid Royal Blue | `#226CF7` | Brighter blue, secondary emphasis / inline links (3×) |
| `--accent-hover` | Deep Ocean Blue | `#1568BE` | Darker accent for button hover |
| `--hl-green` | Highlighter Lime | `#DBFDAE` | Green text highlight (`<mark>`) |
| `--hl-purple` | Soft Orchid | `#F8DCFD` | Purple text highlight (`<mark>`) |

### Lines, borders & semantic states

| Token | Value | Role |
|---|---|---|
| `--line` | `#D9D9D9` | Hairline borders / dividers (source chrome border, t=1) |
| `--success` | `#1D7D3F` | Form success message |
| `--error` | `#D9382F` | Form error message |

> macOS traffic-light dots (`#FF5F57 / #FEBC2E / #28C840`) and the 5%-alpha code-chip
> tints are mockup decoration, intentionally **not** tokens.

### Shadows

Elevation is **deliberately low and soft**. Source shadows are tinted **cool blue-grey
`#717F8C`** rather than black, so they read as ambient haze, not a cast shadow. The effect
is that cards *rest* on the page rather than hover above it — there are no heavy,
high-contrast drop shadows anywhere.

| Token | Value | Elevation feel | Role |
|---|---|---|---|
| `--shadow-card` | `0 0 20px rgba(113,127,140,.06)` | Whisper-soft, even glow | Soft card glow (6× in source) |
| `--shadow-float` | `4px 4px 30px rgba(113,127,140,.25)` | Gently lifted, directional | Floating element |
| `--shadow-mock` | `0 20px 50px rgba(113,127,140,.14)` | Soft drop beneath imagery | Screenshot/mockup drop shadow |
| hero icon | `0 0 60px rgba(0,0,0,.15)` | Wide, diffuse halo | Hero app-icon glow (blur 60 in source) |

---

## Typography

**Family:** `"Plus Jakarta Sans"`, system fallback. Loaded via Google Fonts
(`index.html:13–15`, weights 400/500/600/700/800 + italic-500, `display=swap`). ✅ Loaded.

**Voice:** the type system is built on a single, decisive contrast — **large, bold,
tightly-set headings** in graphite off-black against **soft, medium-weight body copy** in
muted blue-grey. Headings feel assertive and modern; supporting text recedes politely.
Plus Jakarta Sans gives the geometric-humanist warmth that pairs naturally with the
macOS-native feel. Body text never goes darker than slate; pure black is reserved
exclusively for the hero wordmark, making it the single loudest moment on the page.

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

| Token | Value | Physical feel | Usage |
|---|---|---|---|
| `--radius-lg` | 32 px | Generously, pillowy rounded | Large containers, footer top corners (32× in source) |
| `--radius-md` | 18 px | Comfortably rounded | Cards (96× — the dominant card radius) |
| `--radius-sm` | 10 px | Subtly softened corners | Buttons, inputs (source small radius is 10/6 px — **not** 12) |
| `--radius-shot` | 35 px | Generously rounded (single corner) | TOC screenshot top-right corner only (distinct from `--radius-lg`) |
| `--radius-pill` | 100 px | Fully pill-shaped | Pills / round affordances |

There are **no sharp corners** anywhere in the chrome. The shape system reads as friendly
and tactile — every container is rounded, scaling from subtly-softened controls up to
pillowy section cards.

---

## Layout & responsive

**Principles.** A single centred column with **abundant whitespace** is the organising
idea. Content is capped at a comfortable 1160 px and never spans edge-to-edge; text-heavy
sections (FAQ, newsletter) tighten further to 760 px to protect line length and readability.
Sections are separated by **air, not rules** — 84 px of vertical space and the white/grey
band alternation do all the dividing work. Within cards, content is generously padded
(40–56 px) so nothing feels cramped. The whole layout favours one clear idea per row,
centred and unhurried, over dense multi-column packing.

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

A 5-track review compared the shipped code against this system. The
`design-system-refactor` branch then resolved the findings in thin commits.

### Resolved

- **P0 — bento images broken** (doubled `assets/bento/assets/bento/…@1x.png` srcset). Fixed.
- **P0 — bento grid columns voided** by invalid commas (`2fr, 1fr`) → `2fr 1fr` / `1fr 2fr`.
- **P0 — know-card / showcase visuals unstyled** (selectors the markup never set) — wired
  `.know-visual` and pointed image CSS at `.showcase-visual img`.
- **P1 — colour tokens** realigned to source: `--accent` #226cf7→#1874d3, `--surface`
  #f1f4f6→#f3f5f7, `--accent-hover` now distinct (hover was a no-op), `--footer-bg`→#141313,
  `--line`→#d9d9d9; accent-derived alphas via `color-mix()`.
- **P1 — shadows** re-tinted to the source cool-grey `#717f8c`; `--radius-sm` 12→10px.
- **P1 — hero size** now fluid `--fs-hero` (44→72px); no longer overflows on phones.
- **Responsive typography** — single fluid type scale (`--fs-*`) replaces ad-hoc clamps.
- **Layout** — all section boxes aligned to one left edge (bento padding + 940px caps removed).
- **a11y** — global `:focus-visible`; valid hero markup; decorative hero-icon `alt=""`;
  de-duplicated image alt.
- **FAQ chevron** now drawn and animated.
- **Dead CSS removed** — header/nav/mobile-menu (the Final design has no header),
  `.hero-shot-overlay`, `.doc-mock` family, `.reveal`, duplicated grid-area block.
- **Tokens** — `--success` / `--error` added; form JS toggles `.is-error` instead of inline hex.

### Remaining (intentionally deferred)

- **Muted-text contrast** — `--muted` / `--muted-2` are ≈3:1 on white (below WCAG AA 4.5:1)
  and footer whites at `.55`/`.66` are borderline. These are the **source brand colours**;
  darkening them deviates from Sketch. Decision pending: reserve them for large text, or
  agree a darker tint with the designer. Tracked, not silently changed.
- **Spacing tokens** — values are coherent but still literals; a `--space-*` ramp would
  finish the tokenisation. Low priority.
- **`--footer-bg: #141313`** — the only dark fill in the source (appeared once); worth a
  visual confirm against the designer's intent.
