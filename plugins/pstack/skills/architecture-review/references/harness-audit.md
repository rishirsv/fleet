# Agent harness audit

Inspect actual request assembly, instructions, tool schemas and results,
retrieval, compaction and agent coordination. An instruction-only repository
supports source findings; runtime claims require traces from the harness.

## Inspect request construction

Distinguish discovery metadata from loaded instructions and package bytes from
context tokens. Use the shared [workflow measurement rules](../../self-improve/references/workflow-audit.md)
when interpreting session usage. Do not claim exact source attribution
or dollar savings without telemetry and applicable billing evidence.

Look for duplicated instructions, oversized results, repeated discovery,
dependent reasoning split between agents, stale handoffs and missing state after
compaction. Inspect the rendered request as well as its template: ordering,
serialization, timestamps and changing prefixes can defeat cache reuse. Check
provider-supported cache boundaries rather than assuming all stable bytes are
cached. Defer rare tool schemas only if discovery still reliably finds and
invokes them; fewer schemas can increase total work when discovery fails.
Prefer bounded queries, deferred references and accessible source pointers.
Preserve a way to retrieve omitted detail. Independent tasks can use fresh
contexts; merely assigning domain or phase labels does not justify agents.

Recommend changes at the responsible layer. Preserve instruction authority,
required continuation items, permissions and useful information. Compaction
must retain decisions, constraints, unfinished work and access to omitted
sources; compare tasks that actually cross a compaction boundary. Moving text
between message roles changes authority even when the words are identical.
If telemetry is missing, identify a small measurement that could settle the decision rather
than claiming a win.
