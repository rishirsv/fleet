# Make a doc

Create a document (resume, one-pager, memo, letter, report, guide,
paper). First decide which of two shapes the user wants — they export
completely differently:

## Flowing pages

Text that pours onto standard sheets (Letter/A4) and breaks wherever needed:
reports, memos, letters, papers, guides. Write normal flowing HTML. Use the
project's existing print component if one exists; otherwise use print CSS and
`@page` for the requested paper and margins. Claude's `doc-page` component is
not available here and must not be assumed.

Print rules for flowing pages: multi-column text uses CSS columns
(`column-count` + `column-gap`; `column-span: all` on a heading
that spans; `hyphens: auto` in narrow columns — it needs `lang`
on the html element), never side-by-side
flex/grid columns — only real CSS columns flow and break across pages.

Use `break-before: page` on anything that must start a new page (a
chapter, an appendix); add custom kept-together blocks (callouts, stat
tiles, cards) to a `break-inside: avoid` rule and keep each shorter
than a page. Keep headings with their content, keep figures/code/table rows
whole where they fit, and use `orphans: 3; widows: 3` on text blocks.
Do not apply `break-inside: avoid` to multi-column grid rows that cannot fit
on one sheet. Long tables get a `<thead>` so the header repeats on every page.

No `position: fixed`/`sticky` and no viewport units in content —
fixed elements stamp every printed page and `100vh` mis-sizes at print.

## Fixed sheet

A design that must fill exactly one page of fixed dimensions: poster,
infographic, social graphic, certificate. Build at the requested dimensions;
set print geometry explicitly or use an available print component. Check that
content fits the actual target sheet rather than assuming automatic resizing.

Styling (both shapes): body type 14–16px with generous line-height
(1.55–1.7); clear heading hierarchy; restrained palette. Tables get a
header row and hairline borders; figures and code blocks each carry a
short caption. Open with the document's own h1 as the first body
element (use any header-shaped first line of pasted content as that h1
rather than rendering it as a separate masthead).

## Save as PDF

Only when PDF is requested:

1. Read the current HTML design file again; edits or tweak values may have
   changed since an earlier export.
2. Write a fresh print copy from that source. Keep it beside the source so
   relative asset URLs retain their meaning. Preserve typography, colors,
   and imagery. Resolve animations to a visible final state.
3. Use the available PDF or browser-print workflow. Prefer selectable text and
   vector output over screenshot-to-PDF conversion.
4. Inspect pagination, clipping, missing fonts/assets, and the requested page
   count. Deliver the actual PDF, not merely the print copy or export dialog.

Do not assume Claude's print component, version-stamp enforcement, or export
dialog exists in this environment.
