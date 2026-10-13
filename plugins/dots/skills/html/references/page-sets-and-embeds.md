# Linked page sets and embed blocks

## Contents

- [Linked page sets](#linked-page-sets)
- [Plan each page](#plan-each-page)
- [Write the manifest and assemble](#write-the-manifest-and-assemble)
- [Workshop agendas](#workshop-agendas)
- [Embed blocks](#embed-blocks)

## Linked page sets

Use a linked page set when the user requests multiple pages or when a real
ordered sequence needs independent URLs, such as a workshop, course,
walkthrough, or multi-part guide. Keep a short document on one page; do not
split it merely to imitate a website. Every generated file is self-contained
except for relative links to its peers, so move or share the directory as one
unit. Each page must still read coherently when opened directly.

## Plan each page

Outline every page before writing it:

- the reader question or task it owns;
- the supplied content and evidence that belong there;
- the layout and existing components that serve that content;
- the transition to the next page; and
- whether the page also needs an internal `toc-rail`.

Write one body fragment per page, following
[hand-written-pages.md](hand-written-pages.md). Choose each page's layout and
components independently; shared navigation is not a reason to force every
page into the same composition. Use the same design tokens throughout and vary
layouts only when the content differs: an introduction may lead with one
meaningful `wide-figure`, a lab may use parallel evidence in `wide`, and a
wrap-up may close around a single `pull-quote` and recommendation. Keep
prose-led pages in `article`. Do not add imagery, grids, or width merely to
make adjacent pages look different.

For a learning site, use one root contents page, make chapter landing pages
its children, and make lessons children of their chapter. A chapter landing
explains the chapter's learning sequence; the generated `chapter-index` lists
its lessons. Keep live simulations, tutoring, search, and mutable progress out
of a static page set.

## Write the manifest and assemble

Put sequence order, page ids, labels, optional time or context, titles, body
paths, output filenames, layouts, and component names in one manifest. Keep
links between pages out of the body fragments; the assembler generates them.

```json
{
  "schemaVersion": 1,
  "title": "Agentic product workshop",
  "lang": "en",
  "navigationLabel": "Workshop pages",
  "pages": [
    {
      "id": "introduction",
      "label": "Introduction",
      "time": "09:00–09:30",
      "title": "Start with one real task",
      "body": "01-introduction.body.html",
      "output": "index.html",
      "layout": "wide",
      "components": ["timeline", "wide-figure"]
    }
  ]
}
```

`id`, `label`, `title`, `body`, and `output` are required per page. Optional
page fields are `time`, `context`, `dek`, `footer`, `layout`, `components`,
`parent`, and `number`. An optional top-level `tone` applies one tone to every
page.

For a learning site, set each chapter's `parent` to the root id and each
lesson's `parent` to its chapter id. Use `number` for reader-facing labels such
as `2` or `2.1`:

```json
{ "id": "tool-use", "parent": "contents", "number": "2", "label": "Tool use", "title": "Tool use", "body": "tool-use.body.html", "output": "chapters/tool-use/index.html" }
```

Sibling order follows manifest order. The assembler rejects missing parents,
multiple roots, and cycles.

Run `node scripts/assemble.mjs --manifest <manifest.json> --out <directory>`.
The target directory must not exist; the script validates and renders the
complete set before writing it and refuses to overwrite an existing set.
Capture each page with a figure, table, or custom layout as described in
[hand-written-pages.md](hand-written-pages.md#compose-a-body-fragment).

The assembler adds `sequence-nav` for movement between pages. In a
hierarchical manifest it scopes that rail and the previous and next controls to
siblings, generates breadcrumbs, and adds `chapter-index` to parent pages.

## Workshop agendas

- Use `timeline` when time order is the main question and each session
  benefits from a short outcome or description.
- Use a stacked `data-table` when facilitators need exact lookup across
  repeated fields such as time, session, outcome, owner, or format.
- Use prose sections or `process-steps` when the request asks for workshop
  content or a learning arc instead of a clock schedule.
- Put a whole-program agenda on the introduction page when it orients the
  sequence. Do not repeat the complete agenda on every page.

## Embed blocks

An embed block is one component delivered for embedding in another surface,
such as a Notion document, a PR description, or an email. The same visual
style and content rules apply. Package it as follows:

- Wrap the component in `<div class="dots-block" data-component="...">` and
  scope the tokens to that wrapper instead of `:root`. Copy the token block
  from `theme.css` into `.dots-block { ... }`, add
  `background: var(--background); color: var(--foreground); font-family:
  var(--font-sans);`, and rewrite the component's CSS under `.dots-block`. The
  block carries its own background and text style, so it reads as complete
  without inheriting the destination's fonts or theme.
- Remove scripts and reveal animations; the destination controls behavior. If
  the markup has `class="reveal"`, remove it or add `is-in`. The block must
  display completely without JavaScript.
- Omit the TOC, page shell, and general footer. One quiet caption line may
  name an authoritative reader-facing source when attribution helps. Never
  expose tool names, sessions, prompts, private paths, or scratch files.
- For dark mode, pick the variant that matches the destination, or use the
  light background.
