---
name: architecture-review
description: "Audits codebase structure, ownership, domain models, state lifecycles, and opportunities to consolidate or delete code. Use for architecture or structural cleanup reviews; use change-review to review one diff."
---

# Architecture review

Audit the named codebase or subsystem, including existing structural problems
outside a recent diff. A diff review belongs to Change Review. Return architectural findings and
recommendations; this skill does not prescribe an implementation workflow.

## 1. Ground the review

Record the source revision and local changes covered by the audit.
Map the relevant entry points, callers, data flow, state writers, dependencies
and existing checks. Use the repository's vocabulary. Inspect co-changing
modules, repeated corrections, regressions and abandoned attempts when they
could explain structural friction.

Code establishes behavior; contemporary commits, PRs and design records may
establish intent. Separate recorded reasons, inference and unknowns. Preserve
contradictory evidence. A historical reason is a constraint to check against
current requirements, not proof that the boundary must remain.

## 2. Examine the structure

Apply the relevant lenses below. A smell starts an investigation; it is not a
finding without a concrete cost, failure path or simpler supported design.

### Ownership and duplication

Name the current owners of each rule and state value, the surviving owner,
its consumers, and what would be removed. Search for the same decision under
different names: defaults, validation, serialization, cache keys and lifecycle
rules. Distinguish duplicated policy from similar code with different contracts.

At code level, DRY the structure, not every line. Types and data models should converge. Three similar statements still beat a premature abstraction. Prefer explicit over clever.

Information leakage makes multiple modules depend on the same internal decision. A representation, policy, or protocol detail appears in more than one place, so changing it requires coordinated edits.

Look for hand-synced lists that can drift. Keep one list and derive the others from it.

For a disputed responsibility or a non-obvious replacement boundary, use
[ownership and interface design](references/interface-design.md). That reference
owns responsibility placement, boundary depth and caller-first alternatives.

### Reader load

Maintainability is the work a reader must do to understand code. Track two axes: **layers to trace** (indirections between the question and the answer) and **state to hold** (hidden or mutable context the reader must keep in their head). LOC, cyclomatic complexity, and "clean architecture" are proxies. Reader load is the thing that matters. The two axes are independent.

**Make adjacent layers change the abstraction.** A layer that repeats the same methods and arguments adds reader load without compression. Collapse pass-through layers.

**Shrink state scope:** prefer pure functions (returns over mutations), locals over fields, fields over module state, and module state over globals. Derive instead of sync.

Before adding a layer or a piece of state, ask: does it reduce reader load elsewhere by at least as much?

Do not use file length, call-chain length or number of implementations as an
automatic rejection threshold.

### Domain model and access patterns

Encode the real domain in a data structure instead of scattering it across conditionals. A structure that matches the domain makes invalid states unrepresentable and deletes branches. Choosing it at write time is cheap. Recovering it later reads as a refactor and gets deferred.

Reach for:

- A state machine instead of scattered booleans, phases, or lifecycle checks.
- A typed model instead of loose parameters or repeated shape assumptions.
- A map, registry, lookup table, or discriminated union instead of branching spread across files.
- A reducer or command/event model instead of ad hoc state mutations.
- A module organized around one body of domain knowledge instead of a sequence such as load, validate, transform, and save. Execution order is not ownership.
- A small module boundary that gathers repeated behavior, ownership, or invariants.
- A queue, cache, index, graph, tree, or normalized collection where the access pattern calls for it.
- Any other structure that fits. When none fits, work out what the code must never allow and how the data gets read, then find the structure that encodes exactly that.

Do not force an abstraction. Prefer boring code if the current shape is already clear, local, and unlikely to grow. Be skeptical of an abstraction that adds indirection without removing branches, duplicated rules, invalid states, or lifecycle risk.

The sign that you skipped this is a new feature that grows an existing if/else chain by one more branch, or a second boolean that must stay in sync with the first. Temporal decomposition is another sign. Phase-named modules repeat the same domain rules across steps.

Trace the dominant reads and writes through the proposed structure. Check
whether the shape removes coordination or merely moves it into callers.

### Types and system boundaries

Make the compiler reject impossible states, mismatched primitives, and unhandled variants. Prefer defining errors and special cases out of existence over proliferating handlers.

For values that share a primitive representation but have different meanings:

**Brand semantic primitives.** `UserId` and `OrderId` are strings underneath but should not be interchangeable. Give each its own type, such as a branded intersection in TypeScript or a newtype elsewhere.

Don't strengthen everything.
Strengthen a type where an actual use requires a stronger guarantee; returning
an explicit absence or error can be the correct total contract.

**Derive types from authoritative schemas.** When a protocol buffer, OpenAPI spec, GraphQL schema, database migration, design-token file, or another file owns a shape, derive from it instead of hand-rolling a parallel type.

Before writing a property-by-property type guard for external data, look for the repository's runtime schema library and existing schemas. Let one schema own validation and derive the TypeScript type from it. Do not maintain a schema, a duplicate interface, and a guard that can drift apart.

Do not add a new schema dependency for one guard. This rule prefers the schema system the codebase already trusts.

Verify that the parser or guard establishes the claimed invariant. Keep
external, persisted and authorization boundaries explicit; static types do not
prove runtime provenance, freshness or permission. Repeated internal checks
are removable only while the original guarantee still holds across mutation
and asynchronous work.

### Shared state and lifecycle

When concurrent actors might share mutable state, first ask whether they need the same mutable object. If not, eliminate the sharing. When sharing is real, enforce serialization structurally: lockfiles, sequential phases, exclusive ownership. Instructions and conventions are not concurrency control.

Ask: do these actors need one canonical object, or are they publishing independent facts? Give each actor its own owned file, key, branch, or state directory, and merge only at the read/reporting boundary. Two workers writing their own `lastX` field into one `state.json` is still shared mutation. `indexer-state.json` + `metrics-state.json` is not.

Design operations so they converge to the correct state regardless of how many times they run or where the previous run stopped. Every state-mutating operation should answer: "What happens if this runs twice? What happens if the previous run crashed halfway?"

Read the current state, compare it to the goal, and apply only the difference. A step written this way is safe to repeat, because a repeat finds nothing left to do.

Anything a run leaves behind, such as a lock, a temporary file, a half-written record, or a claimed job, must be recognizable as stale by the next run. Judge staleness by evidence that stays true wherever the previous run could have stopped, not only in the common case. A marker that the next run cannot judge turns every crash into manual cleanup. For example, write to a temporary path and rename it into place, or compare artifacts by content instead of by creation order.

Trace acquisition, ownership transfer, cancellation, teardown and restart for
resources and asynchronous work. Identify who releases each resource and what
happens when an operation completes after its caller has gone away. For
irreversible effects, inspect deduplication, transaction boundaries and recovery;
a retry is not proof that an effect happens once.

### Root causes and redesign signals

Ask whether the state that triggered the symptom is legitimate. If the system may be in that state, the code that broke on it is the root cause, and handling the state there is the fix. If the state should never exist, a check where it broke hides the bug. Find what produced the state. Guards, retries, swallowed errors, clamped values, and discarded state are the usual ways to hide a bug.

The signal is a *pattern*, not single instances. Tells:

- The same shape of workaround appearing repeatedly across unrelated code.
- Multiple unrelated edge cases that all need special-case branches.
- Types that need escape hatches (`any`, casts, optional fields always set in practice) to compile.
- The "we need a lock" reflex when the sketch said the state wasn't shared.
- Callers having to know the abstraction's internal rules to use it.

Use judgment. A few edge cases don't condemn an architecture. Some problems are legitimately complex. Complexity in the data is not complexity in the design.

For a supported redesign, ask what shape would fit if the newly established
constraints had been known from the start. Prefer the smallest coherent change
using existing owners.

### Performance and agent harnesses

Use runtime evidence for latency, throughput, retention and contention claims.
Map the profile, retainer chain or blocked thread back to source. Source-visible
structure supports a candidate, not measured savings.

For request assembly, context handling or agent coordination, also use the
[harness audit](references/harness-audit.md).

## 3. Rank and deliver

Return supported candidates in payoff and risk order. Each needs:

- The observed problem and exact source location.
- The proposed change, surviving owner and removed responsibilities or paths.
- The expected benefit, accepted tradeoff and affected callers or data.
- Confidence, the evidence checked, and the check that would establish improvement.

Merge findings with the same cause. Do not invent alternatives, findings or
layers to fill the report. Include material coverage gaps and unproven claims.
A clean audit is a valid outcome.

For each recommendation, name the contracts it must preserve and the evidence
needed to judge it. Distinguish observed problems from untested hypotheses.
