---
name: ask-model
description: "Runs a named model through its Claude or Codex CLI for repository advice, review, or implementation. Use when the user explicitly asks to involve that model."
---

# Ask model

Run the named advisor through its command-line provider. This CLI workflow is
separate from the `consultant` subagent. Read and follow
[CLI.md](references/CLI.md) for current models, effort levels, permissions,
commands, and session handling.

## Set ownership and access

Select one mode before launching:

- **Implementation:** the user asks the named model to implement, build, fix, or
  change something. The advisor owns the repository edits, required checks,
  corrections, and final handoff.
- **Review:** the user asks the advisor to inspect existing work without making
  changes. The advisor returns findings and does not edit the repository.
- **Consultation:** the user asks for advice, design help, or a decision. The
  calling agent retains implementation ownership.

Use the mode implied by the request. Do not silently downgrade implementation
to consultation or take implementation back because local editing is
convenient. Ask only when the request does not establish an owner and the answer
would change the workflow.

Honor the user's choices of model, effort, and access. Implementation normally
needs workspace write; review and consultation default to read-only. State the
actual permission boundary when bypass flags grant broader access.

## Write the prompt

Advisor runs do not inherit this conversation. Write a self-contained prompt
with the task, relevant context and evidence, constraints, mode, ownership, and
completion conditions. Point it at the actual repository so it can inspect the
source directly.

Write prompts, summaries, and recommendations with
[Writing style](../../references/writing-style.md). Supply this reference to the
advisor as a resolved file path it can read, or include its contents in the
prompt, for its authored prose. Preserve quotations and requested verbatim
material unchanged.

For implementation, include this directive near the start:

> Mode: implementation. You own the repository changes, required checks,
> corrections, and final handoff. Use the repository file and terminal tools.
> Do not return only advice or a proposed patch.

## Complete the mode

Preserve verbatim model responses unchanged. Apply the writing style to your
own commentary and synthesis, keeping them separate from the original response.

Wait for the run to finish and inspect its output. For implementation, inspect
the resulting diff and validation evidence. If requested changes are absent or
checks are omitted without a stated blocker, resume the same session with a
focused correction prompt.

For review, return prioritized findings supported by repository evidence. For
consultation, return the recommendation, the evidence and tradeoffs behind it,
and any uncertainty that affects the decision. For implementation, return the
changed files, validation performed, and remaining blockers.

Reconsult only when a new important decision arises or an evidence conflict
remains unresolved; use the same session when context from the first run
matters.
