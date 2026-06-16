# browser_evaluate snippets

Copy-ready functions to pass to the Playwright `browser_evaluate` tool. Each returns plain
data you can assert on.

## Bounding boxes for a set of selectors

Diagnose alignment / width bugs. Differing `left` values across elements that should line up
is the smoking gun (e.g. one section inset by a stray padding, another capped + centred).

```js
() => {
  const pick = (sel) => {
    const el = document.querySelector(sel);
    if (!el) return null;
    const r = el.getBoundingClientRect();
    return { left: Math.round(r.left), right: Math.round(r.right), width: Math.round(r.width) };
  };
  return {
    viewport: window.innerWidth,
    // edit this list to the elements you're comparing:
    a: pick('.showcase-card'),
    b: pick('.bento-card'),
    c: pick('.know-card'),
  };
}
```

## Computed font sizes (verify a type scale)

Confirm a fluid `clamp()` scale lands on the intended px at a given width.

```js
() => {
  const fs = (sel) => {
    const el = document.querySelector(sel);
    return el ? parseFloat(getComputedStyle(el).fontSize).toFixed(1) : null;
  };
  return { hero: fs('.hero-title'), h2: fs('h2'), body: fs('p') };
}
```

Run it at multiple widths via `browser_resize` and compare against the design's min/max.

## Horizontal-overflow assertion

Catches a too-wide element forcing mobile scroll. `overflow:false` is the pass.

```js
() => ({
  overflow: document.documentElement.scrollWidth > window.innerWidth,
  scrollWidth: document.documentElement.scrollWidth,
  innerWidth: window.innerWidth,
})
```

## Force a stylesheet reload (defeat the cache)

When an edit to a linked stylesheet isn't reflected and you've confirmed the server is
sending the new file, the browser cached it. Re-link with a cache-busting query:

```js
async () => {
  const link = document.querySelector('link[rel=stylesheet][href*="styles.css"]');
  await new Promise((res) => {
    const l = link.cloneNode();
    l.href = 'styles.css?cb=' + Date.now();
    l.onload = res;
    link.after(l);
  });
  return 'reloaded';
}
```

Better still, serve with `no-store` headers so this is never needed (see the
`static-site-dev-server` skill).

## Pseudo-element check

Verify a `::before`/`::after` (e.g. an icon/caret) actually renders — `content: "none"`
means the rule didn't apply.

```js
() => {
  const el = document.querySelector('summary');
  const a = getComputedStyle(el, '::after');
  return { content: a.content, width: a.width, border: a.borderRightWidth };
}
```
