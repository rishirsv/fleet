---
name: why
description: "Investigates why code or a design exists from the smallest useful historical record, separating evidence, inference, and unknowns. Use for design rationale, regressions, postmortems, or thresholds; use how for runtime behavior."
---

# Why

Investigate the motivation and intent behind code. Why was it built this way?
What edge cases were considered? What product, business, or operational
constraints shaped the design? What alternatives were rejected, and why?

Why is the companion to `how`. How explains what the code does and how it works.
Why investigates the constraints and decisions that led to the code.

## How this skill works

Historical context is fragmented. It may live in source control, a ticket,
long-form documentation, team chat, observability, error tracking, or product
analytics. Use the code to locate relevant records. Code alone rarely proves intent.

Start with the evidence closest to the change. Widen the search when the direct
record cannot answer the question. Return the strongest answer the available record supports. Search another
system only when its records could improve that answer.

## Evidence rules

- **Collect evidence first.** Decide which explanation the collected evidence
  supports before writing it.
- **Precision over polish.** Prefer a claim the reader can trace to its source
  over a smoother unsupported explanation.
- **Consider what you have not seen.** Ask what evidence would exist if a
  competing explanation were true and whether you looked for it.
- **Name the gaps.** Say when a source is unavailable, linked records provide no further evidence, or
  the record does not answer the question.
- **Match language to confidence.** Use confident language for direct evidence and cautious
  language for inference.

Read [epistemics.md](references/epistemics.md) for the confidence framework,
phrasing guide, and final calibration check. Preserve that confidence language
in the final answer.

## 1. Understand the target

Identify what the user is asking about and what kind of answer would help:

- design rationale: “Why was this designed this way?”
- tradeoff: “Why do we do X instead of Y?”
- defensive reasoning: “What edge case motivated this?”
- external constraint: “What product or operational need led to this?”
- archaeology: “Why does this code still exist?” or “What is the history?”

If the target is vague, use the conversation, current selection, open files, or
recent work to make the best interpretation. State it briefly and proceed so
the user can redirect you.

## 2. Locate the code and its history

Find the relevant files, line ranges, symbols, and recent commits that change
the target's structure, ownership, interfaces, or behavior.
Use blame and file history to locate merge commits, pull requests, tickets,
comments, tests, and incidents tied to the target.

When `gh` is installed and authenticated, inspect the PR body, discussion,
reviews, and linked issues for those commits. Keep the file paths, symbols,
commits, PRs, and ticket IDs together as the starting evidence for later searches.

## 3. Choose the investigation depth

Use the smallest depth likely to answer the question:

- **Focused is the default.** Search source control and the records directly
  linked from the target code and its history.
- **Expanded** adds one to three evidence sources that are likely to hold the
  missing answer. Use it when the direct record is incomplete or contradictory.
- **Exhaustive** searches every available evidence category in parallel. Use it
  for an explicit comprehensive request, a postmortem, a contested or
  high-stakes decision, or when focused searches still support different
  explanations that would change the conclusion.

Read the source file for each category the depth selects. Each file gives
concrete queries for one common tool; adapt it when another tool holds the same
kind of record.

| Category | What it explains | Source file |
|---|---|---|
| Source control | Implementation-time rationale in commits, PRs, comments, and tests | [code-archaeology.md](references/sources/code-archaeology.md) (git, `gh`) |
| Tickets | Customer, product, compliance, or scheduling pressure | [linear.md](references/sources/linear.md) (adapt for Jira, GitHub Issues, Plane, Shortcut) |
| Long-form documents | RFCs, ADRs, PRDs, design alternatives, and postmortems | [notion.md](references/sources/notion.md) (adapt for Confluence, Google Docs, Coda) |
| Team chat | Real-time decisions that never reached a durable doc | [slack.md](references/sources/slack.md) (adapt for Discord, Teams, Mattermost) |
| Observability | Thresholds and defensive code tied to runtime behavior and incidents | [datadog.md](references/sources/datadog.md) (adapt for New Relic, Honeycomb, Grafana, Splunk) |
| Error tracking | Corrective code tied to specific exceptions and releases | [sentry.md](references/sources/sentry.md) (adapt for Rollbar, Bugsnag, Airbrake) |
| Product analytics | Limits, experiments, migrations, and usage assumptions | [databricks.md](references/sources/databricks.md) (adapt for Snowflake, BigQuery, ClickHouse, dbt) |

If the target has null checks, retries, timeouts, rate limits, feature flags,
egress guards, or OOM handlers, also read
[incident-postmortem.md](references/sources/incident-postmortem.md) and run its
incident queries within each selected source.

Investigate directly when the search is small. Delegate independent sources in
parallel when that substantially improves coverage or reduces time. For a large
run, fill [investigator-prompt.md](references/investigator-prompt.md) for each
investigator and append the source file for its category, plus
incident-postmortem.md when the condition above applies.

A search with no results is useful only when its terms and scope could
have found relevant evidence. Record an unavailable source as a gap when it could plausibly change
the conclusion, not as a routine disclaimer.

## 4. Test the explanation

Look for earlier implementations, reversions, contradictions, and evidence that
supports a competing explanation. Do not assume the latest commit tells the
whole story or use a present-day justification as evidence for an undocumented
past decision.

Keep direct evidence, inference, and hypotheses separate while you work. When
several explanations still fit, preserve them instead of choosing one without sufficient evidence.

## 5. Combine the findings

Use a separate synthesizer only when the reports are large, conflicting, or
independently complex. When needed, give it the target code and its history,
findings, searches with no results, skipped sources with reasons, original
question, `epistemics.md`, the output contract below, and
[synthesizer-prompt.md](references/synthesizer-prompt.md). When you relay its
answer, you may lightly edit for clarity or add context from the conversation;
keep its confidence language.

## Output contract

Adapt the headings to the question, but keep the confidence separation:

- **The question.** Restate the decision or history being investigated in one
  or two sentences.
- **The code in question.** Give the relevant files, lines, and symbols in two
  or three lines that orient a reader without prior context.
- **What we found.** One claim per bullet, tagged `[Direct]` for explicit
  single-source evidence or `[Supported]` when several indirect items converge.
  Cite the commit, PR, ticket, document, chat permalink, incident, metric, or
  code comment, with a brief quote or paraphrase.
- **What we can reasonably infer.** Tag claims `[Inferred]`, use language such
  as “appears to,” “likely,” or “suggests,” and show the chain: “Given A and B,
  C is likely.” Skip the section when nothing is inferred.
- **Competing hypotheses.** Include this only when more than one explanation
  still fits. Give each hypothesis, the evidence for it, and the evidence
  against it or missing.
- **What we do not know.** Include this only when a material question remains.
  Name the specific gap: “We searched the issue tracker for [query1] and
  [query2] and found no issue discussing the threshold” is useful; “We don't
  know why” is not. Do not invent a gap to fill the section.
- **Sources consulted.** One bullet per evidence category: what was searched
  (paths, commit and PR counts, ticket IDs, queries, channels and date ranges,
  dashboards, tables and time windows with the numeric summaries that mattered)
  and what it contributed. For a category not searched, say why, such as “No
  matching MCP available in this environment.”
- **Confidence summary.** One or two sentences on overall confidence, naming
  which parts are direct, inferred, or unanswered.

If the question precedes a code change, finish with Preserve / Change / Avoid /
Risk constraints derived from the recorded history.

The investigation is complete when every claim about intent has the right
confidence, material contradictions and gaps are visible, and further searching
is unlikely to change the decision.
