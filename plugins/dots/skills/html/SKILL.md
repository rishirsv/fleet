---
name: html
description: "Creates or edits self-contained HTML pages, linked page sets, embed blocks, and HTML template assets. Use when the result should be a browser-openable document such as a report, plan, or walkthrough; use ui-design for product interfaces."
---

# HTML

Turn supplied material into a self-contained HTML document in the Dots visual
style. Deliver one page by default. Use a linked page set when the parts need
independent URLs, and an embed block when the result goes inside another
surface such as a PR description, Notion page, or email.

Apply [Dots writing style](../../references/writing-style.md) to all visible
prose. Preserve quotations, code, required formats, and source uncertainty.
Explain substantive material visually, following
[Visual explanations](../../references/visual-explanations.md#explain-visually-by-default-in-html).

## Route the task

Read only the references the task needs:

| Task | Read |
|---|---|
| New page from supplied material (default) | [page-modules.md](references/page-modules.md) and [diagrams.md](references/diagrams.md) |
| Quantitative evidence | [charts.md](references/charts.md) |
| Implementation plan, RFC, or proposal for review | [plans.md](references/plans.md) |
| Pull request, commit range, or implemented change | [pr-walkthroughs.md](references/pr-walkthroughs.md) |
| Walkthroughs, code copying, searchable or sortable tables | [interactivity.md](references/interactivity.md) |
| Hand-written body, or editing an existing page | [hand-written-pages.md](references/hand-written-pages.md) |
| Linked page set, course, workshop, or embed block | [page-sets-and-embeds.md](references/page-sets-and-embeds.md) |
| Tone, custom CSS, or visual rules beyond the helpers | [DESIGN.md](references/DESIGN.md) |
| Generated raster imagery | [generated-images.md](references/generated-images.md) |
| A named HTML-template skill | [creating-templates.md](references/creating-templates.md) with `skill-standards` |

## Build and check

Run commands from this skill directory:

```bash
node scripts/catalog.mjs --list               # page helpers
node scripts/catalog.mjs --help <helper>      # signature, rules, example
node scripts/build.mjs <name>.page.mjs --out <name>.html --check
```

`--check` runs `scripts/capture-artifact.mjs` on the built page and writes a
contact sheet and findings file to `<name>.html.capture/`. Use it for every
page with a figure, table, wide or canvas layout, or custom CSS. Fix findings
in the source and rebuild. Before claiming that the page renders correctly,
follow [Visual proof](../../references/visual-proof.md) and name the states
you inspected.

## Deliver

Prefer the platform's HTML creation tool when present. Otherwise write to the
location the user named, or the working directory, and report the path. Name
files and page-set directories for the content (`sync-rollout-brief.html`,
`agentic-product-workshop/`). Describe the delivery state exactly:

- **Standalone:** the self-contained file is ready to open and share.
- **Linked page set:** every page is ready and the directory keeps the
  relative links between pages. It is not hosted.
- **Published:** the user asked for hosting, a publishing workflow completed,
  and the resulting URL was opened and verified. If publishing is unavailable
  or fails, return the standalone file and say it was not published.

## Other callers and boundaries

When another skill loads `html`, use its material, audience, reading order,
and source labels, and report contradictions that would change a claim. When
it supplies `artifact-template.json` with `kind: "html"`, inspect the retained
reference and preview relative to that skill, follow its content and
structure, and deliver the new artifact.

Use `ui-design` for production UI and interactive prototypes, `repo-docs` for
repository documentation, and presentation tooling for slide decks. When the
user explicitly selected Dots Feature Development, apply its
[planning-only boundary](../../references/feature-development.md).
