---
name: ask-model
description: "Runs a named model through its Claude or Codex CLI for repository advice, review, or implementation. Use when the user explicitly asks to involve that model."
---

# Ask model

Run the model the user named through its provider CLI. Read [CLI.md](references/CLI.md)
for launch, stdin, permissions and session handling. Resolve current models
from the active catalog; do not substitute a model or effort.

Infer ownership from the request:

- Implementation gives the advisor the edits, checks, corrections and handoff.
- Review returns findings without edits.
- Consultation leaves implementation with the calling agent.

Do not downgrade requested implementation into advice or take its edits back
for convenience. Review and consultation default to read-only; implementation
needs the requested write access. Disclose broader access when bypass flags
are authorized. Ask only when ownership or access is materially unclear.

Give the advisor the actual repository, goal, evidence, constraints, permitted
side effects and completion conditions. It does not inherit this conversation.
For implementation, explicitly say it owns completing and checking the change.
Keep copied context small and point to source the advisor can inspect.

Wait for completion and inspect the result. Preserve verbatim model output,
separating your synthesis. For implementation, inspect the diff and checks;
resume the same persisted session with a focused correction when work is
incomplete. Reconsult only for a new consequential decision or unresolved
conflict. Report the result, evidence and remaining limits.
