Static marketing site for **Lettera**, a native macOS Markdown editor by Shiny Frog. Plain `index.html` + `styles.css` + `script.js` + `assets/`. No build step, no framework. Deployed to GitHub Pages (`CNAME` = lettera.md).

## Dev

`make serve` — PHP no-cache dev server at http://localhost:8000 (`dev-router.php`). Edits show on a normal reload.

Verify changes visually in a browser before claiming done; mobile responsiveness matters. Skills: `browser-visual-verify`, `static-site-dev-server`, `sketch-design-tokens` (in `.claude/skills/`).

## Design & CSS

`design/DESIGN.md` is the design system source of truth (tokens, type scale, components). Keep it describing the CURRENT state, matching the `--*` custom properties in `styles.css` — it is not a changelog/audit/todo. The editable `.sketch` lives on a shared drive (gitignored).

Tokens live in `:root`; use them, never hard-code values. Fluid type scale via `clamp()` (`--fs-*`). Modern CSS welcome (`color-mix()`, `:focus-visible`, logical properties) — audience is latest Safari/macOS. Favour semantic HTML.

Be brief.
