---
name: shape-idea
description: "Interviews the user to resolve an open idea, plan, or decision, with optional specifications or tickets. Use when the user selects $shape-idea for structured exploration."
---

# Shape idea

Help the user settle an open idea or decision. Preserve supplied goals,
constraints, accepted references and settled choices; recommendations remain
proposals until adopted. Inspect relevant prior attempts and the aspects of
supplied references that bear on the decision. Answer requested factual
questions before asking for choices that depend on those answers.

Create or reuse one conversation-wide `intent.md` using [Intent](references/intent.md).
Update it as decisions evolve, including multiple ideas in the same conversation;
create separate files only when the user requests them.

Map consequential choices and dependencies as a decision tree, including
overlooked failure cases, affected people, durable state, operation, cost and
exclusions. Test vague rules with a concrete “What should happen when…?” case.
Answer factual questions from evidence; ask the user about product choices,
preferences and missing information. Explain conflicts with the current product
before choosing which governs.

Ask answerable questions in small, numbered rounds, most consequential first;
do not ask downstream questions before their prerequisites. Recommend defaults
with useful alternatives and tradeoffs, or ask a simple preference directly.
Teach unfamiliar concepts only as needed for the decision.
Aim for no more than about five questions per round; isolate one when it unlocks
the tree or needs explanation. Respect the user's requested response format.
When appearance or behavior determines a choice, use [Exhibits](references/exhibits.md)
to show a scoped, verified comparison. Keep research and artifacts proportional
to a question or explicit request; use independent research only when it improves
evidence or time, and keep unrelated questions moving.

After each reply, record settled decisions, open choices and what they block.
Keep skipped choices open; reopen settled ones only for new evidence. With
permission, infer answers following a clear pattern and mark those choices.
Do not infer adoption of open choices from a request to plan or build.

Do not start implementation or release while choices needed for that step are
open or direction-changing evidence is pending. Resolve them or agree on a step
they do not block, update the intent, and continue only an authorized next step.
If requested, use [Breakdown](references/breakdown.md) for independently checkable slices with
dependencies and acceptance criteria; otherwise stop at the agreed outcome.
