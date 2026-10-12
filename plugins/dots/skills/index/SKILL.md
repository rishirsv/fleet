---
name: index
description: "Routes a request to the owning Dots skill, shared reference, or Feature Development workflow. Use only when the user explicitly invokes Dots, $index, or Dots Feature Development."
---

# Dots index

Route the request to the smallest Dots workflow that owns it. The index selects
and loads the skill responsible for the work; it does not repeat or replace
its instructions.

## Route only

- When one focused skill clearly matches, load it and follow it directly.
- When several skills apply, choose one primary owner and add only the
  supporting skills needed for distinct parts of the work.
- Read each selected skill or reference before acting on it. Preserve its
  authorization, output, validation, and completion rules.
- Do not turn the skill map into a checklist. Skip routes that do not change
  the work.
- User instructions take precedence over Dots skill guidance. When a skill
  causes a pause or a divergence from the user's intent, name its `SKILL.md`,
  quote the instruction, and separate what the skill explicitly requires from
  your interpretation of it.

## Develop software

For a material feature, bug fix, refactor, measured performance change,
behavior-changing configuration, or implementation plan, read and follow
[Feature Development](../../references/feature-development.md) as the primary
workflow. It routes into focused skills as its phases require.

## Choose the focused owner

Each skill's description defines its boundary. Choose within these groups:

- Design and structure: `$architect`, `$architecture-review`, `$prototype`
- Review and publishing: `$change-review`, `$publish-pr`, `$babysit-pr`
- Explanation and documentation: `$how`, `$why`, `$repo-docs`
- Interfaces and artifacts: `$ui-design`, `$ui-review`, `$html`
- Agent work: `$handoff`, `$meta-prompt`, `$skill-standards`

The user-controlled modes `$ask-model`, `$clarify-requirements`,
`$shape-idea`, `$explain-simply`, `$catch-up`, `$recall`, `$self-improve`, and `$usage-insights`
remain explicit. Load them only when the user selects that mode. Their
descriptions define the exact boundary.

## Load shared references by need

- Read [Hard-cut policy](../../references/hard-cut-policy.md) when replacing a
  schema, contract, persisted shape, route, configuration, value set, or
  architecture, unless the selected skill already loads it.
- Read [Duplicate ownership](../../references/duplicate-ownership.md) when a
  change creates or removes copied policy, competing sources of truth, or
  normalization in several layers, unless the selected skill already loads it.
- During Feature Development, read
  [Performance measurement](../../references/performance-measurement.md) before
  reporting or acting on a measured number,
  [Visual proof](../../references/visual-proof.md) when verifying visible
  output, and [Test consolidation](../../references/test-consolidation.md) when
  placing new or moved tests.
- Load other shared references, such as writing style, visual explanations, and
  session history, through the skill that links them.
