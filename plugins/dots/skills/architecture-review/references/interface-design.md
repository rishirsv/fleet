# Interface design

Generate alternative interface designs when the first plausible interface is
unlikely to be the best one.

## Process

### 1. Describe the problem

Before spawning subagents, write a user-facing explanation of the selected candidate:

- constraints any new interface must satisfy
- dependencies it relies on, classified with the dependency categories below
- the current module boundary and the behavior its implementation handles
- a rough code sketch that illustrates the constraints

This sketch is not the proposal. It helps the user and subagents reason about the same problem.

### 2. Generate alternative designs

Produce two to four meaningfully different interfaces for the deepened module.
For high-impact or non-obvious seams, spawn parallel subagents when available
and independent designs would improve the decision; otherwise create the
alternatives yourself.

Each design should work from the same technical brief: file paths, dependencies
between modules, dependency category, behavior behind the current boundary, repo
review guidance, and relevant domain vocabulary. Give each design a different
constraint:

- Minimal: aim for 1-3 entry points and as much useful behavior as possible
  behind each entry point.
- Flexible: support many use cases and extension points.
- Common path: optimize for the most common caller and make the default case
  trivial.
- Ports and adapters, when applicable: design around cross-seam dependencies.

Each design outputs:

1. Interface: types, methods, params, invariants, ordering, and error modes
2. Usage example showing how callers use it
3. What the implementation hides behind the seam
4. Dependency strategy and adapters
5. Trade-offs: which capabilities callers can use easily and which require more
   work

### 3. Present and compare

Present designs sequentially, then compare them in prose. Contrast by:

- depth
- locality
- seam placement
- adapter need
- test surface

Finish with a recommendation. If elements from different designs combine well,
propose a hybrid. State which design you recommend and why.

## Dependency categories

Classify dependencies before recommending a deepened module. The category
determines how the module is tested across its seam.

### 1. In-process

Pure computation, in-memory state, no I/O. These modules can always be combined
behind a simpler interface. Merge the modules and test through the new interface
directly. No adapter needed.

### 2. Local substitutable

Dependencies that have local test stand-ins such as an in-memory filesystem or
local database substitute. Combine the modules behind a simpler interface if the
stand-in exists. The module is tested with the stand-in running in the test
suite. The seam is internal; no port at the module's external interface.

### 3. Remote but owned

Owned services across a network boundary. Define a port at the seam. The module
owns the logic; the transport is injected as an adapter. Tests use an in-memory
adapter. Production uses an HTTP, RPC, queue, or equivalent adapter.

Recommendation shape:

> Define a port at the seam, implement a production adapter and an in-memory adapter for testing, so the logic sits in one deep module even though it is deployed across a network.

### 4. True external

Third-party services the codebase does not control. The module takes the
external dependency as an injected port; tests provide a mock adapter.
