### Hard cut

Use for a requested hard cut or an internal draft refactor that replaces a schema,
contract, configuration, routing model, or architecture. Keep one canonical
implementation within the requested scope. Existing code alone does not establish
a compatibility obligation.

1. Name the target contract and its owner. Trace its producers, consumers,
   persisted state, and external callers before deciding what can disappear.
2. Establish compatibility obligations. Preserve support required by existing user
   data, on-disk or database state, cross-process wire formats, public contracts,
   or active consumers outside the refactor. Investigate uncertain dependencies
   before removing support. A hard-cut request alone does not authorize data loss.
3. Update all live producers and consumers within scope to the target contract.
   Convert fixtures, builders, snapshots, and tests with them. If a required
   consumer cannot change within scope, treat that dependency as a boundary.
4. Delete obsolete paths and their helpers, branches, flags, comments, and tests.
   Do not retain or add fallbacks, aliases, adapters, coercions, or dual-format
   support solely for abandoned internal contracts. Do not replace compatibility
   handling with guards or tests dedicated to recognizing or rejecting those
   contracts. Keep validation needed for the current contract.
5. Verify the current behavior and any required compatibility boundary. Search for
   remaining old-contract handling and inspect each match. An empty search alone
   does not establish that persisted data or external consumers are covered.

When compatibility is required, isolate it at the actual boundary. Name the exact
file and function, the dependent data or consumer, and why support must remain.
Keep internal code on the canonical contract. Do not invent compatibility layers
elsewhere or expand the refactor to unrelated code.

For a review of a hard cut, apply these criteria within the review's existing
scope. Check callers, fixtures, obsolete paths, and each claimed compatibility
exception. A review request does not authorize implementation.

**Reply:** the canonical contract, removed paths, verification results, and any
remaining compatibility boundary with its evidence or unresolved dependency.

Adapted from Instructa's [hard-cut skill](https://github.com/instructa/agent-skills/blob/main/skills/engineering/hard-cut/SKILL.md).
