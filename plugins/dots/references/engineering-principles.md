# Engineering principles

Apply these when choosing a design or judging a change. This reference owns
design guidance; Design red flags keeps concise diagnostic signs for reviews.

## Model the domain in data

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

## Parse input once at the boundary

Convert external input (requests, files, environment, model output, third-party
responses) into trusted domain types where it enters the system. Inside, trust
those types instead of re-checking them. Validation repeated in several layers
drifts, and code past the boundary that still guards against malformed input
has lost track of where trust begins. Keep framework and transport wiring thin
around that conversion.

Expose domain concepts, not the boundary's private representation. Keep
general-purpose mechanism inside and special-purpose policy at the edge.
Do not re-export transport, storage, framework, or wire types through the
public surface. Keep business logic in pure functions where practical so it
can be tested without the framework.

## Let types rule out invalid states

Model alternatives as explicit variants and handle them exhaustively, so a new
case breaks the build at every place that must change. Give distinct
identifiers distinct types where the language allows. Derive types from one
schema instead of maintaining parallel declarations. Prefer a representation
where an invalid combination cannot be constructed over a runtime check that
rejects it.

## Assume it runs twice or stops halfway

Startup, cleanup, retries, migrations, schedulers, and recovery paths must
reach the same correct result when they repeat or resume after a crash. Before
accepting one, ask what happens if it runs twice in a row, or dies after any
single step. Reconcile against existing state, adopt valid work already done,
and remove stale remnants instead of assuming a clean start.

## Separate writers before adding locks

When parallel agents, jobs, or services could overwrite each other, first give
each one its own file, branch, row, or key. Add locking or serialization only
for state that must be shared, and name its single owner. Separation removes
the race; a lock only orders it.

## Pass the 30-second reader test

A reader should be able to answer a simple question about the code, such as
"where is this value set?" or "what happens on failure?", in about 30 seconds.
If answering takes tracing many layers, remembering distant mutable state, or
reading unrelated files, remove the indirection or move the state next to the
code that uses it.
