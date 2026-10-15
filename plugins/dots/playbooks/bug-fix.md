# Bug fix

**You own this task. Plan, review, verify.** Delegate only when independent investigation or a scoped implementation benefits from it and the host permits delegation. Keep simple fixes local.

Be scientific. Every shipped line traces to runtime evidence. Belt-and-suspenders that "might help" is a hypothesis, not a fix. It does not ship. When evidence refutes a hypothesis, revert what it motivated. The smallest change the evidence justifies ships, nothing more.

1. Reproduce it yourself on the matching surface using the repository's verification skill, existing harness, or available app-control tool, even when a debug or instrumentation protocol says to ask the user to reproduce. Ask the user only with a stated, specific reason the control surface cannot reach the target, and only after driving it as far as it goes. If it won't reproduce directly, synthesize the trigger, tighten conditions, or instrument within the requested scope and budget. If the environment or evidence cannot establish the symptom, report the gap rather than inventing a repro or continuing indefinitely.
2. Binary-search the cause. Form the candidate hypotheses, then rule them out until one survives. Use [How](../skills/how/SKILL.md) when the runtime path is unclear and [Why](../skills/why/SKILL.md) when regression history could distinguish the hypotheses. Each pass, take the split that cuts the most remaining problem space, get runtime evidence, eliminate. When program state is unclear, add instrumentation or logging and read it as the code runs. Don't guess. When two fixes have failed and both rested on the same assumption, test that assumption directly before trying a third. Confirm the surviving *mechanism* with runtime evidence before planning the fix.
3. When the bug has a cheap local test path, write the focused regression test before fixing the code. Choose coverage and establish its failing control under [Test consolidation](../references/test-consolidation.md#regression-signal). When commits are requested, preserve the failing-before and passing-after sequence under the repository's commit conventions.
4. Plan the fix. Use [Architect](../skills/architect/SKILL.md) when a consequential boundary, contract, or state decision must be settled first. If delegating implementation, give the worker a specific scope and use the host's configured model policy.
5. Verify on the same surface. The original repro now passes. "Inconclusive" or wrong-surface is not a pass. Flag it. Unit tests show branch behavior, not bug absence.
6. Finish under [Feature Development](../references/feature-development.md#completion). Run [Publish PR](../skills/publish-pr/SKILL.md) only when publication is requested.

Write the report with [Writing style](../references/writing-style.md).

**Reply:** what was broken, root cause, fix, how you verified. Paste failing-then-passing repro output verbatim.
