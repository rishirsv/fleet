---
name: self-improve
description: "Diagnoses friction in agent work, workflows, skills, or instructions from Codex or Claude session evidence and proposes the smallest durable fix. Use only when the user selects `$self-improve`; not for usage reports."
---

# Self-improve

Learn from agent work and turn supported findings into the smallest useful
improvement. Use counts and helper output to find work that needs inspection;
base conclusions on the conversation, tool calls, files, and observed outcome.
For a report on how the user works with agents, use `$usage-insights`.

## Choose the route

Use the active task unless the user names another task, project, window, or
history. Load only the selected branch:

- **Task reflection, default.** Use current context. Read history only to fill a
  specific gap.
- **Workflow or harness friction.** Read
  [workflow-audit.md](references/workflow-audit.md).
- **Repeated work or a named skill.** Read
  [thread-evidence.md](references/thread-evidence.md). For a named skill also
  read [skill-analytics.md](references/skill-analytics.md).

When a route needs earlier tasks, read
[Session history](../../references/session-history.md). Use the current host
unless the user names another. Analyze Codex and Claude evidence separately
before comparing them.

Run helper commands from this skill directory. Relative `scripts/` paths in
the selected references assume that working directory. Pass `--platform` when
the requested host differs from the current one.

## Evaluate the work

1. Reconstruct the request, intended outcome, actual actions, user corrections,
   and checks that establish the result. A confident completion message is not
   proof by itself.
2. Separate observed causes from plausible explanations. Keep uncertainty when
   the evidence does not establish causation.
3. Before generalizing beyond one task, read
   [thread-evidence.md](references/thread-evidence.md) and apply its
   generalization gate.

Compare the actual actions with the shortest sequence the available evidence
justifies while preserving discoveries that affected the result. State what
worked, what caused problems, how those problems affected the work, and the most
useful next action. A valid result may find no reusable lesson.

For repeated work, choose a fixed set of sessions before reviewing them.
Deduplicate retries and delegated children under the parent session, inspect
examples of success and problems, and preserve contradictions.

For a supported recurring code or harness mistake, read
[enforcement.md](references/enforcement.md) and
[Design red flags](../../references/design-red-flags.md), then fix the class at
the highest level that works.

## Propose or apply improvements

Write proposals, edited instructions, and the report with [Writing style](../../references/writing-style.md).

For a durable change, name the behavior, the component most directly responsible
for it, the smallest change, and how to verify it. For each mistake class,
include its evidence, the enforcement level you picked, and why a higher level
didn't work or would require disproportionate change. Present candidates in
order of severity, using recurrence and strength of evidence to prioritize
findings with similar impact. Include a counterexample or uncertainty only when
it could change the decision. Read [instructions.md](references/instructions.md)
only for proposals targeting `AGENTS.md`, `CLAUDE.md`, `.claude/rules/*.md`, or
review standards, or when a correction repeats an existing rule.

When the request already asks for fixes, apply supported changes within that
scope. Otherwise present the concrete proposal and apply it once the user
agrees. Make changes through the owning workflow, and propose generated-memory
changes for the user to review instead of editing memory stores directly.

Lead with the conclusion. Include only the evidence and coverage needed to
judge it.
