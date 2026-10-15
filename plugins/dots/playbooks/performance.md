# Performance

**You own the measurement story. Plan, review, verify the numbers.** Tie every fix to a measurement, don't read source instead of measuring.

1. Freeze a representative input and baseline. Capture a baseline trace using the repository's verification skill, existing harness, or available profiler.
2. Use [How](../skills/how/SKILL.md) when the runtime path is unclear to ground hypotheses. Don't claim a perf ceiling without running it first.
   Try the performance mantras in order, cheapest first:
   1. Don't do it. Stop work whose result nothing uses rather than cheapening it.
   2. Do it, but don't do it again.
   3. Do it less.
   4. Do it later.
   5. Do it when they're not looking.
   6. Do it concurrently.
   7. Do it cheaper.

   Skip an option when the measured cause rules it out. When an earlier mantra meets the target, stop.
3. Plan the fix from the trace. Use [Architect](../skills/architect/SKILL.md) when a consequential boundary, contract, or state decision must be settled first. Delegate implementation only when it helps and the host permits it, with a specific scope and the host's configured model policy. Review the diff. Capture a post-fix trace using the same input and measurement.
   Verify each attempt before trying the next. Keep measured improvements that preserve required behavior; remove experiments that do not improve the target or violate those requirements.
4. Parse and compare the artifacts (JSON to sqlite, diff). "Inconclusive" or wrong-surface is not a pass. Flag it.
5. Cite the measurement in the report and, when requested, the PR.
6. Finish under [Feature Development](../references/feature-development.md#completion). Run [Publish PR](../skills/publish-pr/SKILL.md) only when publication is requested.

Write the report with [Writing style](../references/writing-style.md).

**Reply:** baseline number, post-fix number, delta, artifact path.
