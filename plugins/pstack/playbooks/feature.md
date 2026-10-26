### Feature

**You own the design and implementation. Plan, build, review, verify.** The main agent does the work by default. Do not delegate merely to separate planning from coding.

1. Ground in the affected subsystem. Use [how](../skills/how/SKILL.md) when the behavior or ownership needs investigation; reuse grounding already established in this task.
2. Use [architect](../skills/architect/SKILL.md) when the interface or module shape needs design exploration. A settled design or obvious local change does not need competing sketches.
3. For work with independent workstreams, write the throughput checkpoint as four todo items. Skip the checkpoint for a straightforward change owned by the main agent:
   - **Blocking first steps.** Gates run before fan-out.
   - **Independent workstreams.** Disjoint files, services, or layers parallelize. Shared writes serialize.
   - **Shared mutable state.** Default to splitting the target. Serialize only for real invariants.
   - **Smallest safe decomposition.** If one worker is best, name why.
4. Implement directly against a specific scope: file paths, the named data shape and its organizing structure, and success criteria. Choose a state machine over scattered booleans, a table/registry over branching, a typed model over repeated shape assumptions, before writing logic. Delegation is optional and discouraged for tightly connected work the main agent can complete. Use [swarm](../skills/swarm/SKILL.md) only when independent bounded slices justify the handoff. Comments follow the [pstack Comments section](../skills/pstack/SKILL.md#comments). Surgical edits, re-ground against the source for upstream-derived files. Port shared-primitive improvements to affected consumers and verify each. Commit only when requested or required by the repository.
5. Verify on the matching surface. "Inconclusive" or wrong-surface is not a pass. Flag it.
6. Build and verify each dependent unit before building on it. When commits are requested, keep them small and ordered; do not rewrite shared history merely to fit this playbook.
7. If the design is contested, use [architecture-review](../skills/architecture-review/SKILL.md) on the disputed boundary. Use [change-review](../skills/change-review/SKILL.md) when independent review of the implementation is warranted.
8. Use [publish-pr](../skills/publish-pr/SKILL.md) when publication is requested or required by the repository.

Code-coupled work (one feature, one migration) goes to a single owner with the checkpoint inline. That owner is the main agent by default and may delegate independent slices after the blocking phase. Parent-level fan-out is for slices that produce independent artifacts (audits, cross-subsystem investigations, competing experiments). Update the checkpoint when the workstreams change. Keep ownership with the main agent across follow-ups.

**Reply:** what you built, what you chose and why, the throughput checkpoint when used, open decisions. Tables for design alternatives.
