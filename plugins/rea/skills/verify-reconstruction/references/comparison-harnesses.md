# Choose a comparison that can catch the mistake

## Common harness contract

For each case retain: original build, candidate build, initial state, input/action
sequence, raw observations, comparison rule and result. Keep original and candidate
output separate. Assert that cases actually ran and required observations exist.
A crash or timeout is a distinct outcome, not an empty result that happens to match.

First run a known matching case. Then intentionally change one expected value or
route one case to an incorrect candidate and confirm failure. Restore the case
before the real run. This checks the path from execution through parsing to verdict,
not merely the equality function. A test corpus with zero selected cases must fail.

Normalize only an irrelevant source of variation that has been identified, such as
a temporary root directory. Preserve distinctions such as absent/null/empty, byte
order, duplicate keys, event order, rounding and error codes when they affect the
contract. Save both raw and normalized observations so differences can be audited.

## Pure functions and binary routines

Use an exported callable or the original program's existing interface first. Calling
an internal address directly requires the exact image/slice, relocation, ABI, hidden
arguments, initialization and valid memory. A C-looking decompiler signature is not
a safe calling declaration. When these cannot be established, use a higher-level
input that exercises the routine through its real caller.

Compare return values plus modified buffers/state. Choose boundary vectors from
the specific instructions and caller constraints, including high-bit values for
signedness and values around truncation or saturation. If fuzzing is useful, record
the seed and minimize failures. Independent published vectors can identify a known
algorithm; the caller's framing, encoding and state still require separate cases.

Byte-for-byte compiled identity is a separate acceptance criterion from behavior.
It may require the original compiler, options and ABI. Do not optimize toward equal
assembly when the task asks for a portable behavioral equivalent.

## Files, parsers and command-line programs

Use paired temporary directories with identical fixtures and record command,
arguments, environment, exit status, stdout/stderr and output files. Check both
acceptance and decoded values; rejection messages may be part of the interface.

Cases should isolate magic/version checks, exact length bounds, ordering, encoding,
trailing data and malformed records relevant to the parser. Compare output bytes
when serialization is the contract; parsing both outputs and comparing objects can
hide formatting, ordering or duplicate-field differences.

## Stateful features

Specify the reset procedure and state scope: process, session, user profile,
database or remote account. Use separate task-owned profiles for original and
candidate. Never reset unrelated user state to make a comparison convenient.

Start with a short sequence: initialize → act → observe → act again → observe.
Add restart and failure/retry only when relevant. A setting that appears correct
until relaunch, a queue that retries twice, or a cache that ignores edits can pass
single-call tests. Capture storage changes and the next operation's behavior.
Minimize a failing sequence by removing actions while retaining the same initial
state and divergence.

## GUI and network features

Define the interaction's preconditions, exact action, completion condition and
observable result. Compare text/accessibility state, enabled controls, files,
clipboard or requests as appropriate. Screenshots establish pixels; they do not
prove persistence, calculations or backend state. Use visual comparison only for
an explicit visual requirement, with fixed viewport, scale, font and appearance.

For a request/response feature, compare method/path, meaningful body fields,
response handling and subsequent local state. Recorded traffic is a finite corpus,
not permission to replay it. A mock built from that corpus verifies client behavior
for those fixtures; it does not establish server semantics or every valid schema.

Control asynchronous completion with an observable predicate (file written, state
shown, request completed), not a fixed sleep alone. Preserve ordering where visible.
For time-dependent or random behavior, fix the clock/seed when the interface allows
it; otherwise compare justified invariants across recorded runs and report variance.

## When execution is unavailable

Produce a runnable harness or fixture plan if requested, and mark it unexecuted.
Static review can still challenge widths, ABI assumptions, state lifetime and missing
branches. Separate that evidence from behavioral parity. Name the smallest missing
resource needed to run: exact matching build, accessible process/device, an input
fixture or an existing observation—not a generic request for “more information.”
