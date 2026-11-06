---
name: shape-idea
description: "Interviews the user to resolve an open idea or decision, rethink an existing product in phases, or turn approved intent into a feature spec. Use when the user selects $shape-idea for structured exploration."
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

## Choose the workflow

- Use **Product design** for a v2 vision, a rethink of an existing experience,
  or a requested phased discovery process.
- When the user brings approved intent and asks for a spec, go directly to
  [Spec handoff](references/requirements-and-design.md#spec-handoff). Carry
  forward prior decisions and surface any new conflict that affects the spec.
- For a bounded idea or decision, use the interview below. A request for a
  spec alone does not trigger Product design. When the interview settles the
  intent and the user has accepted it, use Spec handoff if requested.

## Decision interview

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

## Product design

Read [Requirements and design](references/requirements-and-design.md). Run the
phases in order and label each by number and name. Scale the length of rounds,
exhibits, and outputs to the task. Keep explicitly requested checkpoints and
phase skips. Record skipped work and the resulting evidence gaps. At a pause,
leave the current phase, accepted decisions, and next step in `intent.md`.

0. **Intake.** Ask briefly what product is being reconsidered, why now, and
   where to look, using only questions the supplied context leaves open. Check
   available sources before the interview. Resolve consequential unknowns in
   numbered rounds with a recommendation for each. Present the context brief
   with assumptions marked. **Wait for explicit confirmation before Phase 1.**
1. **Understand today.** Trace the current user journeys and their friction.
   Cite observed behavior and distinguish assumptions and access gaps.
2. **Three points of view.** Compare three distinct ways to deliver the main
   user journeys, including who each serves and what it trades away. Use a
   comparable exhibit when interaction or appearance affects the choice.
3. **Expert critique.** Use the agreed roles to challenge the options, surface
   disagreements, and revise the directions. Treat simulated critique as
   hypotheses. Probe material questions that can be resolved by observation.
4. **Core hypothesis.** Name the change, users, expected outcome, measurable
   signal, and three riskiest assumptions.
5. **Stakeholder interviews.** Explore each group’s needs, adoption conditions,
   and conflicts. Explain how the exercise changes the hypothesis and write a
   short real interview guide. Label simulated responses as hypotheses.
6. **Define A+.** Write five to seven product-specific criteria that distinguish
   A+ from B before drafting the vision.
7. **Vision.** Draft and grade the vision against the rubric. Revise and regrade
   for up to four rounds. Report remaining gaps and evidence needed. Record
   the proposed direction in `intent.md`. **Wait for explicit acceptance of the
   intent before Phase 8.** Reuse acceptance already given for that direction
   and scope when the recorded intent matches it.
8. **Hero flows and user stories.** Draft the feature spec from approved
   intent using Spec handoff. Describe the end-to-end journeys, how they change,
   prioritized stories, and observable acceptance criteria.
9. **Exec summary.** Write a one-page summary and a pasteable implementation
   prompt pointing to the intent and spec. Present the spec for review and
   surface remaining blockers. Start a build only when the user authorizes it.

Carry accepted choices forward into later phases. Reopen a decision when new
evidence changes it or the user asks. At any gate, a request to continue counts
as approval only if it clearly accepts the brief or intent under review. Stop
at the end of a phase when the user requests a pause or the reply needs splitting.
