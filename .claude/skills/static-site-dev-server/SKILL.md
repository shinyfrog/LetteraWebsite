---
name: static-site-dev-server
description: >-
  Add a zero-config, no-cache local dev server to any static site (plain HTML/CSS/JS,
  GitHub Pages, JAMstack output) so edits show up on a normal reload. Use this when the
  user wants to "serve this site locally", "spin up a local preview", "set up a dev server
  for these HTML files", or complains that "my CSS/JS changes aren't showing up on reload"
  / "I have to hard-refresh every time". Reach for it for any static folder that needs a
  quick `make serve` without pulling in a bundler or Node toolchain.
---

# Static site dev server

Drops a tiny PHP-based dev server into a static site. PHP's built-in server (`php -S`) is
on most machines and needs no install or config — ideal for iterating on a hand-written
site or GitHub Pages output without reaching for Vite/webpack.

## Install

Copy both templates into the project root:

```bash
cp assets/Makefile      <project>/Makefile
cp assets/dev-router.php <project>/dev-router.php
```

Then `make serve` starts it on `http://localhost:8000` (override with `make serve PORT=9000`),
and `make open` also opens a browser. Check `php -v` exists first; if the user has Node but
not PHP, offer `npx serve` as a fallback (but it caches more aggressively).

## The one non-obvious thing: caching

The whole reason for `dev-router.php` is that browsers cache `styles.css`/`script.js`, so
edits silently don't appear until a hard refresh — a constant source of "is my change even
working?" confusion while iterating.

The fix has a gotcha worth understanding: a PHP router that does `return false` to let the
built-in server serve a static file **discards any headers the router set** for that file.
So the router can't just set `Cache-Control` and hand off — it must `readfile()` the asset
itself, attaching `no-store` and the right `Content-Type`. The bundled `dev-router.php`
does exactly that (with a path-traversal guard and an `index.html` fallback), and the
Makefile wires it in via `php -S host:port -t . dev-router.php`.

## Should it be committed?

Dev tooling like this is fine to commit so the team shares it, but it's the user's call —
ask if unsure. If the repo *is* the deploy artifact (e.g. GitHub Pages serving the root),
`dev-router.php` is harmless there (it's only invoked by `php -S`, never in production), but
some teams prefer to gitignore local-only tooling. Don't deploy the dev server as the
production server.
