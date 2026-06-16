---
name: browser-visual-verify
description: >-
  Verify a rendered web page with Playwright by *measuring*, not just eyeballing —
  element bounding boxes, computed styles, and responsive assertions across breakpoints.
  Use this when checking a frontend change in a real browser: "verify the layout",
  "check the responsive behaviour / breakpoints", "is anything overflowing on mobile",
  "why don't these sections line up", "confirm the font sizes match the design",
  "screenshot the page and check alignment". The frontend-specialised companion to the
  general `verify` skill — reach for it whenever a visual/layout claim needs proof.
---

# Browser visual verification

Screenshots alone hide pixel-level problems (a 24px misalignment looks fine in a
thumbnail) and tempt guessing. The discipline here is to **measure with `browser_evaluate`
and assert against numbers**, using screenshots to confirm the overall impression. Pairs
with the Playwright MCP browser tools.

## Setup

Serve the page locally (see the `static-site-dev-server` skill if there's no server yet —
and use a no-cache server, or the browser will show stale CSS and you'll chase ghosts).
Then `browser_navigate` to the local URL.

> **Caching trap:** if a CSS change "isn't taking" in the browser but is present in the
> served file, it's the browser cache. Either serve with `no-store` headers, or force a
> stylesheet reload (see `references/snippets.md`) before concluding the rule is wrong.

## Measure, don't eyeball

Use `browser_evaluate` to pull real numbers. The recipes (copy-ready) are in
`references/snippets.md`:

- **Bounding boxes** — collect `getBoundingClientRect()` for a set of selectors to diagnose
  alignment bugs. Misaligned left edges, unexpected widths, and off-by-gutter insets all
  show up immediately as differing `left`/`right`/`width` numbers across elements.
- **Computed styles** — sample `getComputedStyle(...).fontSize` (etc.) at several viewport
  widths to confirm a type scale hits its intended sizes (e.g. fluid `clamp()` reaching
  72px at desktop and ~44px at mobile).
- **Overflow check** — assert `document.documentElement.scrollWidth <= innerWidth` so a
  too-wide hero or unbroken element can't sneak horizontal scroll onto mobile.

## Responsive sweep

Resize with `browser_resize` and re-check at a representative ladder — **mobile 375,
tablet 768, desktop 1280** (add 1440 / 320 for edges). At each width: screenshot, check no
horizontal overflow, and spot-check key computed sizes. State the widths you checked and
the result; don't claim "responsive" from a single viewport.

## Reporting

Lead with the measurements that prove (or disprove) the claim — "left edges now all at
x=44; no overflow at 375/768/1280" — then attach a screenshot for the human. If a check
fails, give the offending numbers and the selector, not a vague "looks off".
