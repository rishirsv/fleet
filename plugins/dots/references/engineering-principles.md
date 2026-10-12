# Engineering principles

Apply these when choosing a design or judging a change. Structural smells such as split ownership and
pass-through layers belong to the design red flags reference.

## Model the domain in data

When the same business rule shows up as scattered booleans and branches,
represent it once: a state machine, a tagged variant, a registry, or a lookup
table. A rule held in data has one place to read and change. Check: can a
reader list every state and transition without searching the call sites?

## Parse input once at the boundary

Convert external input (requests, files, environment, model output, third-party
responses) into trusted domain types where it enters the system. Inside, trust
those types instead of re-checking them. Validation repeated in several layers
drifts, and code past the boundary that still guards against malformed input
has lost track of where trust begins. Keep framework and transport wiring thin
around that conversion.

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
