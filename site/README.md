# Alibi landing page

Static HTML, CSS and JavaScript. No build step, no framework, no analytics.

```bash
python3 -m http.server 8080 --directory site
```

Then open http://localhost:8080.

## Layout

- `index.html` — the page. Sections: hero, app strip, how it works, why it's safe, numbers, pricing, FAQ, closing, footer.
- `css/alibi.css` — tokens at the top (`--paper`, `--accent`, `--ink`…), a tiny reset, then the design system. Change the palette by editing the token block only.
- `js/alibi.js` — header state, reveal-on-scroll, hero screenshot carousel, the tappable phone mock, pricing tabs and the mobile add-on switch, FAQ accordion, and the toast behind the "Get Alibi" button.
- `img/`, `video/` — assets. `img/mark.svg` is the app mark; `img/og.png` is the link-preview card.

## Pricing section

Kept on purpose. Every tier is $0 because the project is MIT licensed; the board is there because it is a nice board. Values live in `PLANS` inside `js/alibi.js`.

## Provenance

The layout and copy are adapted from getvanish.app's landing page and re-themed. Their fonts (SF Pro) were replaced with Inter, their trackers, checkout and licence calls removed, and the copy rewritten where it no longer applied. The phone and Mac screenshots still show the original app's UI and should be replaced with Alibi screenshots once the app exists. The mirrored originals are kept locally in `_source/` (git-ignored, not redistributed); `_source/build.py` regenerates `index.html` and `css/alibi.css` from them.
