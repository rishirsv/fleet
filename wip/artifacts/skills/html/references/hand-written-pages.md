# Hand-written pages and edits to existing pages

Use a hand-written body when the page helpers cannot express the content, a
template supplies its own markup, or only a finished HTML file exists. The
content rules in [page-modules.md](page-modules.md) still apply.

## Compose a body fragment

A body fragment is the page's section markup without the page shell, theme, or
component CSS. `scripts/assemble.mjs` wraps it into a finished page.

1. Select components from `assets/registry/registry.json` by their `when`
   field and read only the matching component source in `assets/registry/`.
   When a valid template manifest is supplied, inspect its retained reference
   instead. The galleries in [the atlas](../assets/atlas.html) and
   [diagram gallery](../assets/diagrams.html) are for human visual review.
2. Choose the width mode: `article` for text with embedded figures, `wide` for
   parallel evidence, and `canvas` for visual references, with prose inside
   `.reading-column`. The assembler supplies `page-shell`: title, short
   introduction (`dek`), footer, and width. It inlines `theme.css` verbatim
   before component CSS; never edit its tokens or add colors inline.
3. Preserve a required reading order and fixed template regions. Give each
   `<section id="...">` an `<h2>` and a short, stable id. Add `toc-rail` for
   six or more sections or a long reference page that needs non-linear lookup.
4. Use `process-steps` for linear sequences and [diagrams.md](diagrams.md)
   when relationships need a figure. Generate the chart forms that
   `scripts/chart.mjs` supports and author others against the same tokens; see
   [charts.md](charts.md). For raster images, follow
   [generated-images.md](generated-images.md) and reference the file with
   `data-embed-src` so the assembler embeds it.
5. Add `page-behavior` when the page needs motion, one-time reveals, TOC
   scroll-spy, or a theme toggle. Give animated charts and diagrams
   `class="reveal"` on their container; leave text sections static.

Write each component with its `data-component` attribute, then assemble:

```bash
node scripts/assemble.mjs \
  --title "Release readiness" \
  --context "project / release" \
  --dek "What is ready, what is blocked, and the next decision." \
  --layout article \
  --body /path/to/body.html \
  --out /path/to/release-readiness.html
```

The assembler includes the registry components named by `data-component` in
the body, plus their dependencies. Use `--components` for extras such as
`page-behavior`. Add `--footer` only when the content calls for it. `--layout`
defaults to `article`; `--tone personal` selects the personal tone. The
assembler packages CSS and behavior; it does not choose components, content,
or section order. Treat the body fragment as the working source: edit it and
reassemble.

Run `node scripts/capture-artifact.mjs --in <page>.html --out-dir <dir>` on the
assembled page, read the contact sheet and findings, and fix them in the body.

## Edit an existing page

Every component instance carries `data-component="<name>"` on its root. To
change one, find the block by that attribute, open the same-named source in
`assets/registry/`, and edit against its structure. Keep the attribute when
copying or adding components so the next editor can find their source.

When the original page module or body fragment is available, edit it and
rebuild. Edit the finished file directly only when it is the only source. A
page built with `--embed-source` can be restored with
`node scripts/build.mjs --extract <page.html> --to <dir>`.
