# Benchmark checklist

Use this reference before relying on a measured speedup, regression, or
performance comparison. It checks the measurement; the
[Performance](../playbooks/performance.md) playbook owns diagnosis and fixes.

Write the claim before running, including the workload, metric, unit, and
comparison. Read the harness to identify what it times, counts, and excludes.
Record the build, configuration, data, machine, and relevant background load.
Use the host's available measurement tools rather than assuming Linux commands.

For an explicitly requested one-run ballpark, check errors, output correctness,
and completed work, then label the result as one observation. Do not use that
exception to select an implementation or claim a speedup.

## Check the measurement

- **Find the limiter.** Collect a diagnostic profile separately from the timed
  runs so instrumentation does not change the reported result. Trace the hot
  path to source and check whether the client or load generator saturates before
  the system under test. Do not explain an unchanged result from source alone.
- **Compare fair configurations.** Use representative builds, flags, versions,
  batching, pools, indexes, and cache state. Tune each candidate for its intended
  production use before choosing between implementations. If equivalent tuning
  is unavailable, report that limit instead of declaring a winner. A deliberate
  configuration comparison should name the settings being compared.
- **Check physical and whole-system limits.** Compare throughput with available
  CPU, disk, or network capacity. Compare claimed end-to-end savings with the
  fraction of time the changed component consumed. Investigate implausible
  results for caches, omitted work, or measurement bugs.
- **Count correct completed work.** Count errors, timeouts, retries, rejected
  requests, and successful operations separately. Inspect result correctness,
  not just file or response existence. Confirm that lazy, asynchronous, or
  optimized code actually executes and completes inside the timed interval.
  Distinguish offered load from successful throughput; a fast rejection is not
  a faster successful operation.
- **Measure variation.** For a comparison, start with at least five runs per
  side and alternate or randomize the sides. Keep warmup and cache treatment
  consistent. Use the established harness's repetition policy when it provides
  stronger evidence. Report per-side run counts, medians, and ranges, including
  noisy runs rather than selecting the best. If variation obscures the gap,
  report no measurable difference or gather enough evidence to resolve it;
  five runs alone do not establish significance.
- **Measure the user consequence.** Pair a microbenchmark with a representative
  end-to-end path when making a product-performance claim. Use realistic data
  sizes and concurrency, and report how much of the whole the microbenchmark
  represents. A helper-only result supports only a helper-level claim.

## Report

Lead with faster, slower, no measurable difference, or inconclusive. Include the
metric and unit, baseline and candidate results, run counts and variation,
limiter evidence, configuration, correctness and work counts, and artifact path.
Reuse the existing measurement artifact instead of creating a second log.

Call a comparative verdict inconclusive when the limiter is unknown, a candidate
is unfairly configured, errors or completed work are unchecked, or the measured
path does not support the claim. Name the missing evidence. Do not turn an
inconclusive benchmark into a reason to ship a speculative optimization.

Adapted from pstack's benchmark checklist, which builds on
[Brendan Gregg's seven benchmarking questions](https://www.brendangregg.com/blog/2018-06-30/benchmarking-checklist.html).
Pinned source and license are recorded in Fleet's maintainer provenance.
