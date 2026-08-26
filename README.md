# Portfolio site

A stripped-down, Futura-set portfolio site for an art historian focused on
Soviet Avant-Garde art. Plain HTML/CSS/JS — no build step, no dependencies.

## Structure

```
index.html         Home
experience.html     Experience — three role boxes
projects.html        Projects — MA / research work
resume.html          Resume — PDF viewer + download
contact.html          Contact — mailto link
css/style.css         All styling and design tokens
js/main.js             Mobile nav toggle + active-page marker
fonts/                 Drop Futura .woff2/.woff files here (see fonts/README.md)
assets/resume/        Drop resume.pdf here (see assets/resume/README.md)
assets/images/          Favicon + any images you add for projects
```

## Before you publish — replace the placeholders

Every editable spot is marked `[PLACEHOLDER]`. Search the project for
`PLACEHOLDER` and fill in:

- Your name (site title, page titles, sidebar)
- Email address (contact page + `mailto:` link + sidebar footer, on every page)
- LinkedIn / Instagram links
- University names on the home page
- Three experience entries (title, organisation, dates, description)
- Four project entries (title, description, and optionally real images
  swapped in for the placeholder SVG thumbnails)
- Your resume PDF at `assets/resume/resume.pdf`

The sidebar (name + nav + footer) is duplicated at the top of each HTML file
rather than pulled from a shared template, since GitHub Pages serves plain
static files with no includes. When you change something in the sidebar
(e.g. your name or email), update it in all five files.

## Adding Futura

See `fonts/README.md`. The site works correctly without any font files —
it falls back to Century Gothic, which is visually close to Futura — but
if you have licensed Futura files, converting them to `.woff2` and dropping
them in `/fonts` with the expected filenames is all that's needed.

## Publishing on GitHub Pages

1. Create a new GitHub repository and push this folder's contents to it
   (this folder should be the repo root, or push it to a `docs/` folder —
   either works as long as you set the Pages source to match).
2. In the repo, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to "Deploy from a branch".
4. Choose the `main` branch and the `/ (root)` folder, then **Save**.
5. GitHub will publish the site at `https://<your-username>.github.io/<repo-name>/`
   within a minute or two.

If you want the site at the root of `https://<your-username>.github.io`
directly (no repo name in the URL), name the repository
`<your-username>.github.io`.

## Notes

- The signature red square (`.mark`) is used throughout as a small nod to
  Malevich and Rodchenko — it appears next to nav items, section labels,
  and the current page indicator.
- The project thumbnails on `projects.html` are original abstract SVG
  compositions, used only as placeholders — swap them for your own
  installation shots, essay covers, or archival material once you have them.
