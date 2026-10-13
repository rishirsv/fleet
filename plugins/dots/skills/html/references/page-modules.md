# Build a page from a page module

A page module is the default source for a new standalone page. It is a small
JavaScript file that calls the page helpers; `scripts/build.mjs` turns it into
one self-contained HTML file. For a hand-written body or an existing page, use
[hand-written-pages.md](hand-written-pages.md) instead.

## Contents

- [Page-module loop](#page-module-loop)
- [Choose the content and structure](#choose-the-content-and-structure)
- [Match each content unit to a form](#match-each-content-unit-to-a-form)
- [Use tables only for tabular information](#use-tables-only-for-tabular-information)
- [Reading orders](#reading-orders)
- [Review before delivery](#review-before-delivery)

## Page-module loop

1. Run `node scripts/catalog.mjs --list` to find a helper, then
   `node scripts/catalog.mjs --help <helper>` for its signature, rules, and
   example.
2. Write `<name>.page.mjs` with `export const kit = "report"` (the required
   selector for the page helpers) and a default function
   `(helpers, data) => page(...)`. Put real `.json`, `.csv`, or `.txt` inputs
   beside the module and name them in `export const inputs`. Strings are
   escaped; the `html` and `svg` tagged templates preserve authored markup, and
   `raw()` is a deliberate opt-out.
3. Run `node scripts/build.mjs <name>.page.mjs --out <name>.html --check`. The
   build fails on missing sources for quantitative helpers, invalid page
   structure, and other helper contracts. `page()` adds a contents list for six
   or more top-level sections and collects distinct sources in the footer.
4. `--check` writes captures and a findings file, `report.json`, to
   `<name>.html.capture/`. Open `sheet.png`, read the findings, and fix them in
   the module. Inspect a full-page capture when the contact sheet cannot show
   the affected area. The check flags desktop figures that scroll inside their
   container, data marks under 24px, and SVGs with a large unused area.
5. Deliver the HTML file. Keep the module and inputs when continued editing is
   useful; they are the working source, so edit them and rebuild. For a
   portable edit loop, build with `--embed-source`. Embedding is opt-in because
   it can put unused input rows or local paths into the delivered file.
   `node scripts/build.mjs --extract <page.html> --to <dir>` restores the
   module and inputs without executing them and refuses to overwrite a
   directory. Inspect extracted code before running it.

`assets/outcomes/status-report.page.mjs` and `decision-comparison.page.mjs`
are complete modules.

## Choose the content and structure

Use a title and a short introduction, then the opening figure chosen under
[Visual explanations](../../../references/visual-explanations.md#explain-visually-by-default-in-html).
Use [diagrams.md](diagrams.md) to pick the form and helper.

- Use `stat-tiles` only for supplied headline measures that matter at first
  glance; omit them when a chart already labels those values.
- Use `recommendation()` only when the request or material commits to a
  decision. Put appendix material (raw data, full logs, candidate configs) in
  `disclosure()` blocks after the main argument.
- Show real chat or text messages with `thread()`, and a sent reply beside a
  suggested one with `exchange()`; the bubble layout lets readers compare
  replies at a glance.
- Add a control when it helps the reader inspect or respond to the document;
  see [interactivity.md](interactivity.md). Use a product-UI workflow for live
  data, external actions, authentication, or complex application state.
- Keep the default tone for work artifacts. Set `tone: "personal"` on `page()`
  for private or relational material written to one person; see
  [DESIGN.md](DESIGN.md#tones).

## Match each content unit to a form

Choose the lightest form that makes the supplied material easier to
understand, compare, or act on. Preserve a strong structure already supplied
by the caller or source.

| Content | Form |
|---|---|
| Explanation, background, rationale, narrative | Prose under descriptive headings; bullets only when they improve scanning |
| Decision, constraint, or takeaway the reader must not miss | A short lead callout with nearby evidence |
| A real sequence, runtime path, or procedure | `process-steps`, when order changes meaning |
| Requirements or loosely related factors | Grouped bullets |
| Actions or acceptance checks a reader will mark | Checklist; never decorative status checkboxes |
| Terms, responsibilities, key facts | Compact labeled prose, or `file-map` when code responsibility matters |
| Alternatives with shared criteria | `comparison-grid` for a few concise cases; `data-table` for exact rows or many criteria |
| Relationships, boundaries, branching flows | A diagram; see [diagrams.md](diagrams.md) |
| Quantitative evidence whose pattern matters | A chart; see [charts.md](charts.md) |
| Evidence, citations, continuation links | A quiet source list without internal working material |

## Use tables only for tabular information

Use a table for repeated items with shared fields when lookup or comparison is
the point. If most cells become sentences, switch to prose, bullets, steps,
callouts, or disclosures. Size columns by their content: keep identifiers and
states compact and give explanatory text room. On narrow screens, preserve
labels and meaning through wrapping or a documented responsive treatment
instead of shrinking text below a readable size.

Check whether adjacent tables or repeated component forms make the page
harder to read. Change a form only when another representation fits the
information better.

## Reading orders

Use these only when the caller and source lack a deliberate order. They
arrange supplied content and never invent a claim, fill an evidence gap, or
make a decision the source did not make. For an explanation of a code change,
use the order the `how` skill supplies.

- **Plan:** goal and scope → visual overview of phases and dependencies →
  full steps, owners, constraints, and verification.
- **Decision:** context → visual comparison → distinguishing evidence →
  recommendation.
- **Explanation:** answer → visual overview → mechanism → worked example →
  implications.
- **Status:** current state → meaningful movement → blockers → owned next
  actions.
- **Incident:** impact → chronology → established cause → recovery →
  follow-up.
- **Comparison:** criteria → meaningful differences → trade-offs → decision,
  or an explicit statement that there is none.

## Review before delivery

- Each figure explains a relationship the prose does not already make
  obvious, and every value traces to a source.
- For each material finding in the source, the page keeps its consequence and
  evidence; it includes an action only when the source or request supports
  one.
- The page is self-contained and makes no external requests.
- The page uses the design system and semantic HTML, keeps native tab order and
  visible focus, labels controls, gives informative figures equivalent text,
  and pairs color with text, shape, or line style.
- Internal working details, prompts, private paths, scratch files, and
  generation metadata are gone.
- The page leads with the subject. It omits directions about how to read or
  respond unless the interaction needs them.
