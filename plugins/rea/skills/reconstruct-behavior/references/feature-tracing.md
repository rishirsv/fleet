# Trace a feature from trigger to effect

Use this guide when the requested behavior crosses functions, processes, storage,
or a service boundary. Follow one concrete input through the actual application.
For a target-only request, inspect its entry points and principal app-owned
components, choose a representative path, and return the resulting explanation
and useful next investigation. Build a replacement only when requested.

## Establish the observable path

Choose a trigger from the user's example: a click, command, input record, route,
error, displayed value, or captured request. Record the starting state and the
observable result that would answer the question. Trace:

`trigger -> input conversion -> validation -> state/computation -> effect -> result`

Follow initialization, error handling, and persistence when they change this
path. Expand to a neighboring component only to resolve a named missing link.
Separate application logic from framework plumbing and third-party libraries;
inspect dependency internals when the requested behavior actually depends on them.

A screenshot supplies layout, text, values, and candidate interaction targets.
Use its labels to search resources or code and its visible states to plan probes.
It cannot establish event handlers, computation, network contracts, or hidden
states. For a visual recreation, implement the evidenced appearance and label
behavioral choices that the reference does not settle. For behavior recovery,
find the underlying application or capture before attributing implementation.

## Browser and Electron applications

Use the [JavaScript guide](../../reverse-engineer-anything/references/javascript-applications.md)
for artifact analysis, source recovery, graph selection, and version comparison.
Use the [runtime guide](../../reverse-engineer-anything/references/runtime-observation.md)
for supported observation and actions.

- Start at the supplied route, visible label, module, IPC channel, endpoint, or
  error string. Inspect its local handler before widening the graph. Read nearby
  source maps and lazy chunks when the handler imports code outside the first bundle.
- Trace browser events into state/store actions, selectors, and rendering. A
  displayed value may be formatted, cached, or derived from a different underlying
  value. Inspect both the write and the read that reaches the screen.
- In Electron, trace renderer calls through the preload bridge to main-process
  handlers, then storage, utility processes, native bindings, or network clients.
  Match actual arguments and response/error shapes at each boundary. A shared
  channel string is a lead; dynamic channel construction needs further evidence.
- For a `.node` boundary, identify the requested binding and exported operation
  before native analysis. JavaScript wrapper behavior may answer the question
  without reconstructing the entire native dependency.
- If static edges are ambiguous, observe the smallest relevant interaction and
  correlate the handler, arguments, request, or state change. A registered handler
  does not prove that the user's interaction reaches it.

## Native functions and data

Use the [native guide](../../reverse-engineer-anything/references/native-and-artifacts.md)
for provider details, memory/file mappings, metadata, and annotations.

Before interpreting a suspicious function, check its calling convention,
arguments, return use, and relevant caller. Wrong decompiler prototypes can make
ordinary code appear to contain impossible pointer arithmetic or control flow.
Recover the contract from call sites and instructions; keep uncertain fields
explicit rather than cleaning pseudocode into a confident but invented type.

For a consequential branch, inspect the exact compare and extension operations.
Track operand widths, signedness, truncation, overflow, and comparison order.
For a buffer, establish length units, checked range, offset arithmetic, alignment,
and byte order before describing its layout. Distinguish file offsets, analysis
addresses, and runtime addresses when following pointers or tables.

When a value comes from global state, find its writers and initialization path.
When a call is indirect, inspect the dispatch table, object type, or runtime
target needed to resolve it. Do not fill unreadable memory with zeros or assume
an unresolved call has no effect. Recognize algorithms through constants and
operation order, then test independent vectors; resemblance is only a lead.

## Stateful feature recipes

**Search:** trace input normalization, debounce/cancellation, query construction,
local versus remote execution, ranking/filtering, and result presentation. Test
an empty query, a discriminating match, and two rapid queries when stale results
are plausible. Preserve ordering and state in the comparison; a set of matching
rows can conceal wrong ranking or an outdated response winning a race.

**Sync:** identify the local mutation, queued representation, identity/version
fields, outbound operation, acknowledgment, and local reconciliation. Examine
retry, deduplication, conflict, and deletion paths only as relevant to the request.
Use a bounded sequence with a known starting state; successful transport alone
does not establish successful reconciliation. A capture may reveal protocol
shapes while leaving offline queues and conflict policy unknown.

**Export:** follow selected state through filtering, ordering, transformation,
serialization, and destination writing. Inspect the produced artifact as well as
the completion UI. Probe a boundary relevant to the format, such as escaping,
encoding, empty output, or numeric precision. Compare semantic contents first
when timestamps or container metadata vary; retain raw files to ensure the
normalization does not discard meaningful formatting or ordering.

## Choose the next action from the missing link

| Current gap | Next useful action | Result that resolves the gap |
|---|---|---|
| Only a label or screenshot | Search matching resources/strings, then their readers | Candidate handler or view location |
| Handler exists, output unexplained | Trace its argument transformations and consumers | Input-to-output path |
| UI and stored values differ | Inspect formatter/selector and storage read/write | Units, rounding, cache, or persistence rule |
| IPC or indirect target ambiguous | Inspect construction/dispatch or observe one invocation | Actual target and transferred values |
| Decompiled branch is inconsistent | Check caller contract and decisive instructions | Correct types, bounds, or comparison |
| Behavior differs across runs | Control initial state; inspect initialization and timing | State or ordering dependency |
| A request is known but its cause is not | Correlate one interaction with the request builder | Trigger and request relationship |
| Proposed implementation disagrees | Minimize input/sequence and compare intermediate effects | Earliest divergent operation |
| Required runtime unavailable | Continue static/captured evidence at the unresolved boundary | Bounded claim and exact missing observation |

After each resolved link, update the current feature path and the next unresolved
decision in the investigation notes. Resume from that decision, reusing matching
artifact analysis and captures. Do not rerun broad discovery merely because a
new session began.

## Captured traffic and service boundaries

Treat HAR, SAZ, packet traces, logs, and saved responses as observations of their
recorded sessions. Extract the relevant request/response shapes, ordering, and
error cases with their coverage. Observed optionality does not establish all
valid inputs; a client request does not reveal the server's internal algorithm.

Inspecting a capture does not require replaying recorded URLs or credentials.
Keep reconstruction local when only captured behavior is available. If the
requested feature depends on an unavailable service, specify the observed
boundary and use an explicit fixture or adapter for a requested implementation.
Report which behavior the fixture covers and which service behavior remains
unobserved. Never present fixture agreement as verification against the service.
