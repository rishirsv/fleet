# Ownership and interface design

Use this when a supported architecture candidate needs an ownership decision
or a replacement interface. Do not generate alternatives for an obvious local
simplification.

## Locate the responsibility

Use the repository's actual responsibilities and modules. Do not impose a
generic layer scheme.

Read the repository's architecture and boundary records, then trace the actual
call and state flow. If records and code disagree, name the difference. Label
ownership inferred from code when the records leave it unresolved.

Choose by who must enforce the invariant, not where the symptom appeared.
Allow separate presentation or transport representations when they protect
different contracts. A shared representation is not automatically a shared policy.

For a disputed placement, distinguish these owners using concrete modules and symbols:

- The runtime owner executes or coordinates the behavior today.
- The first-fix owner is where the immediate defect can be corrected without
  leaving other callers inconsistent.
- The canonical long-term owner enforces the rule for every relevant caller.

These owners may coincide. When they differ, explain why the immediate fix is
insufficient, which responsibility moves, which competing owner disappears, and
which boundary code remains. A recommendation does not authorize that move.

Runtime dispatch does not automatically own reusable product policy. Place
presentation state with its UI owner, platform behavior with its platform owner,
and vendor details with the integration. Use the repository's actual contracts
to decide exceptions. Do not move pure logic into shared code merely because it
could be reused.

## Design the boundary

An interface includes everything a caller must know: types, operations, errors,
ordering, configuration, lifetime and performance guarantees. Judge it by useful
behavior hidden behind that knowledge, not method count or internal file size.

Apply the deletion test: imagine removing the module. Does complexity disappear,
or does necessary logic spread into callers? Preserve boundaries that hide
real complexity. Internal implementation can remain composed of small parts
without exposing each part to callers and tests.

A seam needs a current responsibility. Keep translation at external, persisted,
or untrusted boundaries even with one adapter. Introduce a variation interface
when implementations actually vary; do not invent a second adapter to justify
an otherwise unnecessary abstraction.

Do not confuse a deep module with a deep call chain. A deep call chain scatters understanding across layers. A deep module concentrates capability behind one interface.

Look for these signs:

- Callers coordinate several methods to complete one operation.
- Public options expose internal stages or implementation choices.
- Learning the interface does not save the caller from learning the implementation.

## Compare caller-facing designs

Start with the concrete use case, existing boundary, constraints and invariants.
For a consequential uncertain boundary, compare materially different designs.
An obvious local simplification does not need manufactured alternatives.

Sketch actual caller usage when it helps distinguish the alternatives. The usage is the spec. The two must agree, so reconcile the sketch to the usage, not the reverse.

For each viable design, show the core data structures, operations, state owner,
errors and dependencies. Compare what callers must know, what complexity the
module hides, the places a change touches and the behavior testable through it.
Explore flexibility only for current callers, not hypothetical extensions.
Recommend a path and name accepted tradeoffs.

## Boundary enforcement

Check whether callers can bypass the intended owner by importing internals or
mutating its state directly. Identify where the design relies on conventions
that its types or module boundaries could enforce.
