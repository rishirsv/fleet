---
name: skill-standards
description: "Creates, updates, or statically reviews Dots plugin skill source against Dots standards. Use when authoring, revising, or diagnosing a Dots skill; not for behavioral evaluation or plugin packaging."
---

# Skill Standards

Read [standards.md](references/standards.md) for every task. Apply
[Writing style](../../references/writing-style.md) while writing instructions
and again before completing a review; its
[prose-finding form](../../references/writing-style.md#report-a-prose-finding)
sets how to report each prose defect.

For creation or updates, use the environment's default `skill-creator` for
authoring mechanics, resource structure, validation, and forward testing.
Plugin scaffolding, manifests, packaging, marketplace entries, installation,
and cache updates belong to the default `plugin-creator`.

For a static review, read [skill-review.md](references/skill-review.md).
Review-only requests leave source unchanged; when the user also requests
fixes, apply the supported edits.

When the user wants the current or a named Codex task turned into a new or
updated skill, read [session-capture.md](references/session-capture.md).

When the skill being authored produces visual artifacts whose layout affects
correctness, read [Visual proof](../../references/visual-proof.md) for how its
instructions should have the agent render and inspect them.

Return the changed source, or the review verdict, findings, and proposed
edits, with the checks performed and any uncertainty that still affects use.
