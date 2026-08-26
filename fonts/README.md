# Adding your Futura files

The site already falls back to Century Gothic / Avenir Next, which are close
enough to Futura that the site looks correct with **zero setup**. If you want
true Futura, convert your files to `.woff2` (and optionally `.woff` for older
browsers) and drop them into this folder using these exact filenames:

```
fonts/
├── futura-book.woff2      (regular / weight 400)
├── futura-book.woff
├── futura-medium.woff2    (medium / weight 500)
├── futura-medium.woff
├── futura-bold.woff2      (bold / weight 700)
└── futura-bold.woff
```

`css/style.css` already has `@font-face` rules pointing at these filenames —
you don't need to touch the CSS. Any font file you don't provide simply falls
back gracefully.

### Converting a .ttf/.otf to .woff2

If you only have `.ttf` or `.otf` files (e.g. from Adobe Fonts or a purchased
license), the quickest free conversion is:

- [cloudconvert.com/ttf-to-woff2](https://cloudconvert.com/ttf-to-woff2), or
- the `fonttools` command line: `pip install fonttools brotli` then
  `fonttools varLib.instancer` / `fonttools ttLib.woff2` — see the
  [fonttools docs](https://fonttools.readthedocs.io/).

Only use font files you're licensed to use. Futura is a commercial typeface
(Bauer Types / Monotype); this repo does not include or redistribute it.
