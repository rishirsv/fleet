---
name: shape-idea
description: "Interviews the user through every branch of an idea's decision tree, surfacing known and unknown unknowns, and can split the result into tickets or specifications. Use only when the user selects `$shape-idea`."
---

# Shape Idea

Help the user settle an open plan, decision, or idea by working its decision
tree until no consequential choice is left unasked or silently assumed.

## Start with what is known

Extract the desired result, constraints, preferences, examples, accepted
references, and decisions the user has already supplied, and treat them as
settled. An accepted reference or stated direction governs intent; when the
current product, code, or documentation conflicts with it, explain the
difference and ask which should govern.

Look for earlier attempts at the same idea, such as half-built, reverted, or
abandoned work in the repository or its history, and learn why they stopped.
Those reasons often name the hardest decisions.

## Find the unknowns

Map the idea as a **decision tree**: each decision connects to the later
decisions that depend on it. Fill it from two directions:

- **Known unknowns:** open choices the user has named or the request implies.
- **Unknown unknowns:** consequential questions the user has not raised, such
  as failure and edge cases, who else is affected, data and state that must
  survive, operation and rollout, cost, and what the idea should refuse to
  become.

Challenge assumptions that do not serve the user's goal, and prefer a simple,
coherent idea over accumulated complexity. When a word is ambiguous, state your
interpretation and let the user correct it. Test a vague rule with a concrete
case: "What should happen when…?"

## Ask the frontier in rounds

The **frontier** is every decision whose prerequisites are settled: the
questions answerable now without guessing at answers not yet given. Ask the
frontier together in one round. When it holds more than about five questions,
ask the most consequential first and keep the rest for the next round, because
long rounds get skimmed. Ask a question alone when it unlocks much of the tree
or needs focused deliberation. A question that depends on another question in
the same round belongs to a later round.

Number each question, put the decision first, and recommend an answer worded
so that "yes" accepts it:

```md
**Q1 · <plain-language decision>**

<Why it matters and what changes with the answer.>

- **A · <option>**: <what it means in practice, its strongest benefit, and its
  main cost.>
- **B · <option>**: <same.>

**Recommendation: A.** <Why it fits the direction so far and which tradeoff
makes it preferable.> Reply "yes" to accept.
```

Ask a simple preference or open judgment directly, without a choice list. Frame
questions in the user's terms: what they would see or do for product work;
behavior, ownership, and boundaries for code, leaving implementation details to
a later plan; and the decision supported, audience, definitions, and evidence
for analytical work.

Teach only what the decision needs. When an option involves a concept the user
may not know, add a short **What these mean** list below the recommendation
that says, in a sentence or two each, what the option commits them to and how
to tell whether it fits. Skip concepts the user already uses confidently. When
several concepts need real teaching, ask that question alone.

When the user cannot judge a choice from prose, show an exhibit. Read
[Exhibits](references/exhibits.md) to choose and prepare one, and follow
[Visual proof](../../references/visual-proof.md) to confirm it renders before
asking for a judgment.

## Keep facts and decisions apart

Facts are your job; decisions are the user's. Look up anything the repository,
tools, or external sources can answer instead of asking. Inspect directly for a
focused lookup, and dispatch a subagent when independent research, fresh
alternatives, or a small prototype would improve coverage or time. A pending
lookup blocks only the questions downstream of it, so keep asking the rest of
the frontier while it runs. Bring back what a finding means for the choice
along with its source and uncertainty.

When answers form a clear pattern, offer once to answer the remaining questions
that match it on the user's behalf. If they accept, show each answer you chose
and mark it as yours in the snapshot so the user can reverse it.

## Update the tree after each reply

Record newly settled decisions, recompute the frontier, and briefly name the
consequential choices still open. Keep a skipped question open and ask it again
when it returns to the frontier. Reopen a settled choice only when new evidence
changes or contradicts it. A request to plan or build accepts the settled
direction; it does not answer a skipped question that could change the work, so
show what remains and keep shaping.

## Finish when the frontier is empty

The session ends when every consequential decision is answered, rejected, or
explicitly deferred and no pending finding could change the direction. Return
an Idea Snapshot using [the snapshot template](references/snapshot.md) so the
next workflow can continue without reopening the interview.

When the user wants the work split up, also turn the settled tree into tickets
or specifications using [Breakdown](references/breakdown.md).

If the user has already authorized the next step, continue into it. Otherwise
state the next mode in the snapshot and ask before acting on the result.
