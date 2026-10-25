# Agent harness audit

Inspect actual request assembly, instructions, tool schemas and results,
retrieval, compaction and agent coordination. An instruction-only repository
supports source findings; runtime claims require traces from the harness.

Distinguish discovery metadata from loaded instructions and package bytes from
context tokens. Measure per completed task when usage exists: input and cached
input, output, turns, retries, latency and child work. Cached tokens are already
part of input; do not add them again. Cumulative usage and transcript length are
not current context occupancy. Do not claim exact source attribution or dollar
savings without telemetry and applicable billing evidence.

Look for duplicated instructions, oversized results, repeated discovery,
dependent reasoning split between agents, stale handoffs and missing state after
compaction. Prefer bounded queries, deferred references and accessible source
pointers. Preserve a way to retrieve omitted detail. Independent tasks can use
fresh contexts; merely assigning domain or phase labels does not justify agents.

Recommend changes at the responsible layer. Preserve instruction authority,
required continuation items, permissions and useful information. If telemetry
is missing, identify a small measurement that could settle the decision rather
than claiming a win.

Compare changes on a fixed set of real tasks using completed outcomes and
material failures alongside time and usage. Inspect tasks that improved and
regressed. Keep null results and limitations visible; another team's reported
percentage is not a forecast for this harness.
