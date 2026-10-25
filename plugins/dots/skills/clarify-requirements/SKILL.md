---
name: clarify-requirements
description: "Resolves ambiguous requirements before implementation through focused questions. Use when the user selects $clarify-requirements; use shape-idea to explore an open idea."
---

# Clarify Requirements

Inspect the request, repository guidance, configuration, accepted references,
and nearby code before asking. Never ask for an answer already available.
Clarify only when plausible answers change the objective, definition of done
(including edge cases), scope, constraints, or safety boundary.

Ask the smallest set of unresolved questions: at most three initially, most
consequential first, none if evidence settles them. Keep questions short;
number multiple questions. Offer distinct choices and a recommended default
when useful, including “not sure, use the default” when it eases answering.
Separate blocking decisions from optional preferences.

While a blocking decision remains unresolved, continue only low-risk inspection;
do not edit files or give a detailed implementation plan. If the user authorizes
proceeding without answers, state consequential assumptions and continue without
asking for confirmation again.

For meaningful scope or risk, briefly summarize the agreed outcome, definition
of done, scope and non-goals, constraints, and remaining assumptions. Use plain,
precise language. Establish requirements rather than an implementation plan.

Clarification is complete when blocking decisions are answered, explicitly
deferred, or covered by user-authorized assumptions. Stop for clarification-only
requests; otherwise continue implementation already authorized. Do not reopen
settled decisions without new evidence; report evidence that changes a decision
before continuing.
