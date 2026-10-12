# Insights report

Contents: scope, reading `stats` fields, sections, coverage, output template.

The report covers the whole retained session window for the selected host. Its
sections and judgments read the same whichever host supplied the sessions: say
"the agent" for the assistant side and name the host only in the coverage block.

## Scope

Profile the whole retained window for the selected host, rather than a subset
selected for problems. The profile needs the distribution across all sessions;
triage selects the sessions most likely to contain useful evidence.

Run the statistics pass first, then read a small number of representative
sessions to explain what the numbers mean:

```bash
python3 ../self-improve/scripts/self_improve.py stats
```

`stats` caches derivations by schema, session, transcript mtime, and effective
time bounds, so closed sessions inside successive windows reuse their cache and
sessions crossing a moving boundary are recomputed. It scans the full selected
window by default. `--limit` and `--max-new` impose explicit caps; include
eligible, analyzed, included, skipped, malformed, and interrupted counts in the
report. A completed scan does not imply complete telemetry or an unbiased
profile.

Sessions with fewer than two user messages or under a minute of elapsed time are
flagged as weak narrative evidence. They remain in workload totals when they
contain recorded tools or token samples, including delegated children. Empty
sessions and transcripts whose opening turns are a usage report or self-improve
pass are excluded and counted separately. Without `--days`, the bounds cover
retained history through the current clock; pass `--days` only for a narrower
window the user requested.

## Reading `stats` fields

- **Engaged time** sums consecutive event gaps under 15 minutes; report it as
  time worked. **Session span** is first-to-last wall clock, includes idle and
  resumed time, and can exceed the calendar window.
- **Host-injected blocks** are instruction and context payloads sent with the
  user role but never typed. They are excluded from message volume and keyword
  signals.
- **Interruptions** count the host's interrupt sentinel plus short imperative
  stop turns. A zero can mean the host records no sentinel.
- **Failure buckets** show broadly where problems occur. An empty set can mean
  the failure markers do not match this host's tool surface.
- **Testing time** shows how long recorded tests and builds took, which
  repeated, and whether failures were followed by edits and another test. Read
  the conversation before explaining why.
- **Tool counts** separate raw outer calls, orchestration wrappers, and
  recorded command/MCP operations. `tool_calls` excludes `exec` wrappers and
  includes distinct structured operations; wrapper children without a recorded
  parent link stay unattributed. Prefer structured status and exit codes;
  `inferred_tool_failures` and `unknown_tool_outcomes` mark heuristic or missing
  evidence. Other completed-item kinds are not operation-normalized.
- **Tokens** are nonnegative differences between successive cumulative samples
  inside the requested bounds, with boundary-crossing intervals, counter
  resets, missing fields, and sample-less records disclosed. Treat missing
  cache/reasoning fields as unknown. Cached input is included in
  input and reasoning in output, so do not add them twice. Convert traffic into
  money only with billing evidence.
- **Lineage** identifies declared parent/child records and parents outside the
  included set. Children exclude events before their creation; unknown forks,
  retries, or recaptured inherited events stay in the counts. Record totals are
  not a count of independent tasks, so inspect the parent cluster before
  attributing workload or generalizing.
- **Time bounds** apply to stamped events. Unstamped events are counted as
  unavailable and excluded from bounded measurements. Test-call durations can
  overlap, so their sum is not elapsed wall time.
- **Unmeasurable** lines name capability gaps. Repeat them in the coverage
  block instead of reporting a zero as a finding.

Statistics describe volume and distribution. A durable change needs the
evidence record and generalization gate of `$self-improve`.

## Sections

Write in second person. Skip a section rather than padding it.

1. **How you work**: a few paragraphs on interaction style, such as quick
   iteration or detailed upfront specs, interrupting or letting a run finish,
   and how corrections arrive. Ground each claim in a `stats` distribution or a
   session you read. Bold the observations that determine the conclusion.
2. **Project areas**: the main areas by session share, each with what the work
   was and how the agent was used.
3. **What is working**: the workflows the evidence shows are worth keeping. Skip
   flattery, tool-call trivia, and restated raw counts.
4. **Where friction appears**: split the two sides, because each needs
   different fixes. *Agent-side*: misread requests, wrong approach, output that
   did not work. *User-side*: thin context up front, environment and setup
   gaps, scope that shifted mid-run. Give each side concrete patterns.
5. **Quick wins**: draw from what is installed and configured. An installed
   skill with no organic invocations in `skill-usage` or `stats` is a stronger
   lead than a feature pitch. Skip suggestions that amount to "give more
   context" or "confirm before acting".
6. **On the horizon**: ambitious workflows the evidence suggests better models
   could make reachable, such as autonomous loops, parallel agents, or
   iterating against tests.
7. **Leads for self-improve**: patterns that look durable enough for a
   `$self-improve` review.

## Coverage

Close with a coverage block that states:

- the host inspected, and whether the other host's state was present but unread;
- the window requested and the retention boundary (a missing older session is
  not evidence the work never happened);
- sessions listed, analyzed, excluded, and capped;
- capabilities the host did not record, such as absent event timestamps, which
  rule out a response-gap distribution; and
- whether malformed rollout lines were encountered.

## Output template

```md
# Usage insights

<sessions> sessions · <messages> messages · <hours>h engaged · <commits> commits
<window start> to <window end>

## At a glance
- **What's working:** <short summary> See _What is working_.
- **What's hindering you:** <agent-side, then user-side> See _Where friction appears_.
- **Quick wins to try:** <installed, unused capability> See _Quick wins_.
- **Ambitious workflows:** <what better models unlock> See _On the horizon_.

## How you work
## Project areas
## What is working
## Where friction appears
### Agent-side
### User-side
## Quick wins
## On the horizon
## Leads for self-improve
- Lead: <pattern>
  Why it might be durable: <one sentence>
  Next step: run `$self-improve` on this lead

## Coverage
- Host: <selected host>
- Window: <range> · retention limit: <limit>
- Sessions: <analyzed> of <listed> · excluded: <counts> · capped: <count>
- Unmeasurable: <capabilities the host did not record>
```
