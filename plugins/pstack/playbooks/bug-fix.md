### Bug fix

**You own this task. Plan, review, verify.** Investigate and fix directly. Delegate independent investigations through [swarm](../skills/swarm/SKILL.md) when useful; keep diagnosis and integration with the main agent.

Be scientific. Every shipped line traces to runtime evidence. Belt-and-suspenders that "might help" is a hypothesis, not a fix. It does not ship. When evidence refutes a hypothesis, revert what it motivated. The smallest change the evidence justifies ships, nothing more.

1. Reproduce it yourself on the matching surface with the available browser, simulator, CLI or native UI tools, even when a debug or instrumentation protocol says to ask the user to reproduce. Ask the user only with a stated, specific reason the control surface cannot reach the target, and only after driving it as far as it goes. If it won't reproduce directly, synthesize the trigger, tighten conditions, or instrument until it fires.
2. Binary-search the cause. Form the candidate hypotheses, then rule them out until one survives. Use [how](../skills/how/SKILL.md) over the affected subsystem and [why](../skills/why/SKILL.md) for regression history when those questions remain unresolved. Each pass, take the split that cuts the most remaining problem space, get runtime evidence, eliminate. When program state is unclear, add instrumentation or logging and read it as the code runs. Don't guess. Use [figure-it-out](../skills/figure-it-out/SKILL.md) if the user invokes it for a substantial uncertain investigation. Confirm the surviving *mechanism* with runtime evidence before planning the fix.
3. Plan the fix. Use [architect](../skills/architect/SKILL.md) when the fix requires a new or uncertain interface; crossing a function boundary alone is not enough. Implement the smallest change the evidence justifies.
   For persistent or asynchronous behavior, apply the
   [correctness checks](../skills/change-review/SKILL.md#correctness) while implementing.
   This uses the checks without starting a separate review.
4. Verify on the same surface. The original repro now passes. "Inconclusive" or wrong-surface is not a pass. Flag it. Unit tests show branch behavior, not bug absence.
5. When the bug has a cheap local test path, capture the failing case before the fix and confirm it passes afterward. Skip a new regression test when it would be expensive, integration-heavy, unclear, or merely mirror the implementation. Preserve the failing-then-passing evidence. Commit only when requested or required by the repository.
   When adding or moving coverage, or after creating diagnostic probes, apply
   [test consolidation](test-consolidation.md) before final verification. Reuse
   the test-admission decision and failing-then-passing evidence already established.
6. Use [change-review](../skills/change-review/SKILL.md) when independent review is warranted. Use [publish-pr](../skills/publish-pr/SKILL.md) when publication is requested or required by the repository.

**Reply:** what was broken, root cause, fix, how you verified. Paste failing-then-passing repro output verbatim.
