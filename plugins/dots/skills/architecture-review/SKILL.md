---
name: architecture-review
description: "Audits codebase structure, ownership, duplication, and opportunities to consolidate or delete code. Use for architecture or structural cleanup reviews; use change-review to review one diff."
---

# Architecture review

Audit the named codebase or subsystem for structural problems, including
existing problems outside a recent diff. A diff review uses Change Review.

Trace current behavior, callers, state, tests and relevant design records.
Use the repository's vocabulary. Code establishes behavior; commits, PRs and
contemporary records may establish intent. Distinguish recorded reasons,
inference and unknowns, and preserve evidence that contradicts a proposal.

Look for competing state or policy owners, shallow forwarding layers,
unnecessary concepts, duplicated tests and obsolete paths. Before deleting a
boundary, ask where its complexity goes: retain translation for real external
or persisted contracts. Name the owner that should retain each responsibility
and the callers or data that depend on it. Prefer the smallest coherent change
using existing owners; sketch caller usage before proposing a new interface.

Use independent read-only investigators only for bounded evidence paths that
can proceed independently. Keep connected reasoning and integration local.
For an agent harness, also read [harness-audit.md](references/harness-audit.md).
For performance claims, use the conditional [benchmark checklist](../../references/benchmark-checklist.md).

Return ranked, actionable candidates: the observed problem and source, the
concrete change or deletion, expected payoff, confidence, and the check that
would establish improvement. Do not invent alternatives or layers to fill a
report. Source-visible structure supports a candidate, not measured savings.

An audit-only request ends with recommendations. When implementation is
already authorized, apply supported changes within scope, preserve required
behavior and compatibility, and verify the affected paths. Ask only for a
remaining decision that materially changes the work.
