---
name: html-authoring
description: Create or edit standalone HTML documents, visual explanations, plans, code walkthroughs, prototypes, and small task-specific editors. Use when the deliverable is an HTML file or linked set of HTML files.
---

# HTML Authoring

The entrypoint follows artifact-design's structure; references retain
mode-specific guidance. Source ownership and adaptations are recorded in
[source notes](references/sources.md), not required reading during authoring.

## Page contract

**Format and skeleton.** For standalone output, write a complete `.html` document
with doctype, language, charset, viewport, head, and body. Use a fragment only
when the chosen host explicitly requires one. Preserve the substance of supplied
material rather than transcribing Markdown one-to-one.

**Title.** When the user already has a specific name for the thing, use that name
for the title rather than coining a new one. Keep it stable across revisions.

**Runtime.** Use only capabilities present in the actual delivery surface.
Ordinary page controls need no service integration.

## Read the request first

Many requests call for a more utilitarian treatment: a plan, a memo, a demo.
Make it polished, with real typographic hierarchy, considered spacing, and a
proper palette, but avoid over-designing. Most pages don't need a flashy,
gigantic hero. Keep flourishes tasteful and limited.

Some requests call for an editorial treatment: a landing page, a game, an app
or tool they'll keep or share.

If unsure: a well-composed page is always acceptable; an over-designed visual
identity sometimes isn't.

Use one file by default, linked pages when separate reading paths are useful,
and the existing application's stack when the requested change belongs there.

## Use cases

The following headings retain Thariq Shihipar's use-case structure. Select the
relevant form; these are capabilities, not sections required on every page.

### Specs, planning, and exploration

Compare approaches beside one another; make tradeoffs and unresolved decisions
visible. Expand the chosen approach into mockups, interfaces, data flow, and an
implementation plan as needed. Keep related artifacts linked and readable by
another agent without the originating conversation.

### Code review and understanding

Use real source and diffs, anchored annotations, and diagrams of the behavior
being explained. Preserve file and revision references. Present existing review
findings without inventing a new review pass or changing their severity.

### Design and prototypes

Render tokens, component variants, states, and interactions. Where tuning is
useful, expose controls and an export of the chosen parameters. Reuse the
project's design system; mark simulated behavior and example data.

### Reports, research, and learning

Organize evidence into a reading path with suitable tables, charts, diagrams,
and explanations. Keep provenance, units, assumptions, and uncertainty near
the claims they qualify. Support both scanning and closer inspection.

### Custom editing interfaces

Build a small editor for the specific data: triage, ordering, annotation,
configuration, prompt tuning, or selection. Provide a usable export such as
JSON, changed keys, annotations, or a prompt. Keep edits in the artifact until
the user asks to apply them elsewhere; copying a result does not apply it.

## Fundamentals for every artifact

Read [design fundamentals](references/design.md) for page composition. It owns
layout, typography, themes, charts, UI copy, and editorial treatment here.
Read only the additional references needed for the artifact:

| Task | Reference |
|---|---|
| Mechanism, data flow, architecture comparison | [Artifact diagramming](references/diagrams.md) |
| Printable report, memo, fixed sheet, PDF export | [Make a doc](references/documents.md) |
| Prototype, tweaks, design options, persistence or live state | [Interactions](references/interactions.md) |
| Self-contained offline file | [Save as standalone HTML](references/standalone-html.md) |
| Email-client HTML | [HTML email](references/email.md) |

## Shared design and components

Use [DESIGN.md](DESIGN.md) and [components](references/components.md) when no
project design system is supplied. Edit linked HTML/CSS directly; the optional
`scripts/export_html.py` creates a portable copy with local CSS and scripts
embedded. Keep source separate and make targeted edits across follow-ups.

## Process

Start from what the viewer should be able to do on the page, in addition to what
they will read.

Reuse the project's tokens. Otherwise define the colors, type, and spacing the
page needs in `:root`, then build from them. Keep design planning in the working
file; no separate plan or fixed number of fonts and colors is required.

**Write, check, deliver.** Use the available browser skill to preview the file,
or serve it locally when the browser cannot open file URLs. Inspect the reading
layout, narrow-screen behavior, and the main interaction. For an editor, change
a value and inspect the export; for charts, compare marks and labels with data.
Fix concrete defects and recheck affected behavior. Do not rerun passing checks
or add review agents by default. If preview is unavailable, report that limit.

Deliver a clickable link to the actual file or linked directory. A preview is
not a downloadable export. Use the selected service's tools only when import
or publishing is requested; a local file is not a hosted page.

## Ownership

This skill owns HTML composition, interaction, packaging, and delivery. Existing
planning, explanation, and review skills retain ownership of their reasoning
and findings. Design owns broader product-design work; Drafts owns long-form
prose development; Canvas owns import and editing inside Canvas. None is a
mandatory dependency for a standalone HTML file.
