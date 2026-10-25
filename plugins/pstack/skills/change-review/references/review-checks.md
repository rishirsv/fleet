# Review evidence

Trace contracts, state transitions, retries, cancellation, errors, empty inputs
and replaced guards through real callers. For deleted logic, identify its
invariant and surviving owner. For wrappers and caches, verify forwarding uses
the intended instance without recursion. Language-specific hazards require a
concrete reachable case, not a generic warning.

For downstream risk, identify the fact safety depends on. Look beyond symbol
searches at persisted data, wire formats, configuration, scheduled jobs and
other consumers. Prove the fact with source or a small read-only probe when
practical; an empty text search alone cannot establish absence. Preserve real
external and user-data compatibility while deleting obsolete internal paths.

For simplification, show what can disappear while preserving behavior. Prefer
existing owners; examine duplicate rules, state that can be derived, forwarding
layers, speculative abstractions and abandoned code. A boundary is useful when
its necessary complexity would reappear in callers if removed. Keep translation
at real external boundaries. Do not confuse familiar local repetition with
competing policy owners. Match changed-line style to the repository, leaving
formatter-enforced details to tooling.

Tests should reject a plausible broken behavior and survive internal refactoring.
Derive expected results independently. Flag vacuous assertions, production logic
inside doubles, broad snapshots unrelated to the contract and duplicate coverage
that adds no failure signal. Preserve privacy, persistence, concurrency, retry
and lifecycle contracts before deleting tests. Existing passing results establish
only the behavior they exercised. Exact UI claims need rendered evidence.

Trace untrusted input through authorization, parsing, storage and external writes.
Check scaling, retained resources and meaningful performance claims. Every retry
needs a reason, refreshed state or backoff and a stopping bound. One failed batch
item should not prevent independent items from completing.

For an omissions sweep, reread the assigned diff and enclosing functions looking
only for missing defects, especially moved guards, default changes and asymmetric
setup/teardown. Verify new candidates yourself and return one combined result;
an empty sweep is valid.
