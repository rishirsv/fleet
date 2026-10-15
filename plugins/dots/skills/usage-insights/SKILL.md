---
name: usage-insights
description: "Reports agent-usage patterns and provides feedback on prompting and steering from Codex or Claude sessions. Use when the user selects $usage-insights; use self-improve to change workflows or instructions."
---

# Usage insights

Report how the user works with agents. Use counts and helper output to choose
what to read and to describe distributions; base conclusions on the
conversations, tool calls, and outcomes you read. Evaluate the work in scope,
never the person's intelligence, personality, or general potential.

These reports describe; they leave instructions, skills, memory, scripts, and
the harness unchanged. When a pattern looks durable enough to change, report it
as a lead and offer to run `$self-improve` on it.

## Choose the report

Write the report with [Writing style](../../references/writing-style.md).

- **Coaching or rating.** The user wants a reflection on, evaluation of, or
  rating for how they prompt, reason, steer, decide, or work with agents. Read
  [coaching.md](references/coaching.md).
- **Usage insights.** The user wants a broad profile of how they use agents
  across retained history. Read
  [insights-report.md](references/insights-report.md).

## Read session history

Use the active task unless the user names another task, project, window, or
history. When the report needs earlier tasks, read
[Session history](../../references/session-history.md). Use the current host
unless the user names another, and analyze Codex and Claude evidence separately
before comparing them.

The session helper belongs to the sibling `self-improve` skill. From this skill
directory, run it as `python3 ../self-improve/scripts/self_improve.py`, and pass
`--platform codex|claude` when the requested host differs from the current one.

Return markdown by default. When the user wants a shareable page, apply `$html`
to the finished report and use its output-location guidance.
