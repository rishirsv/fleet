---
name: dots
description: "Routes a request to the owning Dots skill, shared reference, or Feature Development workflow. Use only when the user explicitly invokes Dots, $dots, or Dots Feature Development."
---

# Dots

Route the request to the smallest Dots workflow that owns it. Dots selects
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

## Follow the current task

Continue the selected workflow on follow-ups such as "do it" or "continue,"
within the outcome and permissions already established. When the user changes
the outcome or switches between investigation, planning, implementation, or
review, select the owner again and apply the new stopping point. Carry forward
relevant facts and settled constraints, not the previous workflow's remaining
actions. Answer an interim question or status request, then resume the active
task unless the user changes or stops it. "New task" makes a switch explicit
but is not required. Ask only when those readings would lead to materially
different work.

## Develop software

For a material feature, bug fix, refactor, measured performance change,
behavior-changing configuration, or implementation plan, read and follow
[Feature Development](../../references/feature-development.md) as the primary
workflow. It routes into focused skills as its phases require.
Use `$agent-workflow` instead when the user wants the whole plan-to-PR flow
run with delegated agents.

## Choose the focused owner

Each skill's description defines its boundary. Choose within these groups:

- Design and structure: `$architect`, `$architecture-review`, `$prototype`
- Review and publishing: `$change-review`, `$publish-pr`, `$babysit-pr`
- Effects beyond a named diff: `$blast-radius`
- Explanation and documentation: `$how`, `$why`, `$repo-docs`
- Documents: `$html`. Product interfaces use `$design` and `$design-review`
  from the separate Design plugin when installed. If unavailable, complete the
  task directly with existing product sources and Dots visual-proof guidance.
- Agent work: `$ambition`, `$handoff`, `$meta-prompt`, `$skill-standards`

The user-controlled modes `$ask-model`, `$clarify-requirements`,
`$shape-idea`, `$explain-simply`, `$catch-up`, `$self-improve`,
`$usage-insights`, and `$verification-skill`
remain explicit. Load them only when the user selects that mode. Their
descriptions define the exact boundary.

## Load shared references by need

- Read [Hard-cut policy](../../references/hard-cut-policy.md) when replacing a
  schema, contract, persisted shape, route, configuration, value set, or
  architecture, unless the selected skill already loads it.
- Read [Duplicate ownership](../../references/duplicate-ownership.md) when a
  change creates or removes copied policy, competing sources of truth, or
  normalization in several layers, unless the selected skill already loads it.
- Load other shared references, such as writing style, visual explanations, and
  session history, through the skill that links them.
