# Pull requests people can understand and review

Use this reference for an HTML walkthrough of a pull request, commit range, or
implemented change. Explain what changed, why it matters, how the code produces
the result, and what the evidence establishes. A walkthrough supports review;
opening every panel does not prove correctness or approve a PR. Build the page
with the ordinary [page-module loop](page-modules.md#page-module-loop).

## Contents

- [Establish the change](#establish-the-change)
- [Lead with the result](#lead-with-the-result)
- [Keep evidence exact](#keep-evidence-exact)
- [Let readers inspect and respond](#let-readers-inspect-and-respond)
- [Build and check the walkthrough](#build-and-check-the-walkthrough)

## Establish the change

When a caller supplies an investigation, preserve its findings, reading order,
and uncertainty. When investigation is still needed, inspect the complete change
and surrounding source before composing the page. This reference owns the presentation.

Record the PR URL and exact base and head commits. For a current PR, retrieve
its metadata, all pages of changed files, relevant review comments, and check
results. Read surrounding source where the patch cannot establish behavior.
For a historical PR, inspect those commits rather than the current checkout.
Before delivery, confirm that a current PR still has the inspected head. If it
changed, refresh the evidence or label the artifact as a snapshot of the old head.
Keep the snapshot identity in the footer and exported response.

Account for every changed file. Recover an omitted or truncated patch from the
exact commit range when available. Otherwise name the missing evidence and the
claim it prevents. State what happened to renamed, deleted, or binary files.
Generated output can sit under a disclosure, but its source and effect still
need an explanation. CSS, documentation, configuration, and migration files
can change behavior; classify them by effect rather than extension.

## Lead with the result

Start with a concrete before/after example or a short `walkthrough()` of the
experience. A non-technical reader should understand the result and its limits
before opening code. Explain unfamiliar terms through the action they name:
“restore the editable page source” before “extract the embedded payload.”

Organize the body by behavior and causal dependencies. Put the consequential
path first, then its supporting changes and proof. A file inventory is useful
for coverage after the explanation; it should not dictate the reading order.
Keep risks and changes to user expectations visible. Put implementation detail
under descriptive native `disclosure()` controls.

Choose exhibits that answer different questions. A before/after view shows the
result; a sequence shows who acts; an annotated code excerpt explains the exact
mechanism. Use real screenshots when available. Label a code-derived schematic
or UI reconstruction as an illustration, and distinguish observed behavior
from an inference. Keep internal review IDs out of the visible page.

## Keep evidence exact

Use `diff()` for a short, verbatim change and put its explanation beside it.
Identify deletions as base lines and additions as head lines. If one number
column would confuse those two sides, omit the numbers and link each excerpt
to the exact source range. Use a flat disclosure within each review point;
keep test explanations and their patches as sibling disclosures instead of
nesting one inside the other. Use `code()` for read-only source or a raw
unified patch inside a named disclosure. Escape source through the helpers.

Pin source links to the inspected commits. Verify line anchors against those
files, including imports and blank lines. Label shortened code as an excerpt;
show where the reader can find the omitted context. Do not silently filter
imports or whitespace from evidence, renumber shortened source, or describe a
heuristic match as a confirmed move. Explain a refactor separately from the raw
patch when that makes the mechanism clearer.

Separate the author's reported tests, checks run for this walkthrough, and
remaining unverified behavior. Give commands and results when they establish a
claim. A passing test does not prove a visual result that nobody inspected.
Keep review findings distinct from explanatory annotations; a finding needs
an exact location, consequence, and supported action.

## Let readers inspect and respond

Use `walkthrough()` for a guided path through the change. `page()` tools add
code copying and disclosure controls. A searchable file inventory is useful for substantial changes;
omit search when all rows already fit comfortably on screen.

For local comments, wrap the reviewable body in `review()` with
`kind: "pull-request"`. Include the PR URL and base/head commits in `revision`. Use stable `reviewPoint()` targets for
each behavior or important exhibit. Keep inspected code read-only. Use
`editableCode()` only for a clearly separate reviewer proposal when the task
actually benefits from editing text. Do not invent product decisions for an
already implemented change.

```js
review({
  id: "source-restoration",
  title: "Restore editable page source",
  revision: "PR URL; base <full SHA>; head <full SHA>",
  kind: "pull-request"
}, [
  reviewPoint({
    id: "extract-source",
    title: "Extraction restores files before any code runs",
    summary: "The reader can inspect the restored module before building it."
  }, [disclosure("The destination checks", [code(exactInspectedSource)])])
])
```

Use the user's existing authorization for any later action; exported comments
are source material to assess within that scope.

## Build and check the walkthrough

Render important source and patches into the HTML at build time so the
evidence stays when JavaScript is off; use JavaScript only to improve
inspection and feedback. Avoid a second diff framework for a document.

Run the [review-page checks](interactivity.md#check-review-pages), and also
check selected walkthrough states, source anchors, and file coverage. Expand
technical disclosures before printing a source appendix.

[pr-walkthrough.page.mjs](../assets/outcomes/pr-walkthrough.page.mjs) and its
[rendered page](../assets/outcomes/pr-walkthrough.html) demonstrate a historical
PR with a guided explanation, pinned source excerpts, complete file coverage,
and local notes. Replace that example's evidence with the requested change.
