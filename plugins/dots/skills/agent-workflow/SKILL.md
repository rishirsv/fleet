---
name: agent-workflow
description: "Runs a feature from plan to a reviewed, babysat pull request in one flow: plan, spec, build, review, PR, and babysit, delegating each stage to the right agent. Use only when the user selects `$agent-workflow`."
---

# Agent workflow

Run the whole delivery loop as one orchestrated flow. You are the coordinator:
you hold the plan, write each agent's brief, check each stage's gate, and keep
the user informed. Agents do the reading, writing, and reviewing.

Hold the plan as an explicit stage table instead of improvising turn by turn,
and keep intermediate results in files and artifacts instead of the
conversation. That makes the run repeatable, lets you resume it, and keeps your
own context for decisions.

## Options

The user can add options in any order, for example
`$agent-workflow add CSV export review=high stop-after=spec`:

- `review=low|medium|high|xhigh|max` sets the `$change-review` level
  (default `low`).
- `stop-after=plan|spec|build|review|pr` ends the run after that stage.
- `approve=spec` pauses for the user's approval after the spec. Without it,
  pause only for product decisions, approvals the repository requires, and
  irreversible actions.

## Orchestration patterns

Use these four patterns, whatever tools the platform provides:

- **Delegate:** one agent, one brief, one structured result.
- **Parallel:** independent tasks at once, then wait for all of them.
- **Fan out per item:** the same step for each file, unit, or finding.
- **Gate:** a stage ends only when its check passes. Retry a failing check
  until it passes or two rounds make no progress, then stop and report.

Verify before you trust: send each consequential finding or claim to an
independent agent that tries to disprove it. Run parallel writers only on
disjoint files or in isolated copies such as separate worktrees; otherwise run
them in sequence. Keep runs small, under about five agents at a time unless the
user asks for more, and try a small slice first when cost is uncertain. When the
platform has a native workflow engine and the user asked for one, express the
fan-outs as a workflow script; without subagents, run the same stages yourself
and keep every gate.

## Choose the agent

| Role | Use for | Writes files |
|---|---|---|
| `explorer` | read-only investigation of one question | no |
| `consultant` | a focused second opinion on a decision or plan | no |
| `architect` | one complete proposal for interfaces, types, and state | no |
| `worker` | a well-specified change in an assigned scope | yes |
| `luna` | hard or ambiguous implementation that needs judgment | yes |
| `adversary` | independent critique of a spec, a change, or a claim | no |

Use the Dots agent definitions when the platform loads them. Otherwise start a
fresh subagent and give it the role's description as the first line of its
brief. Never let the agent that wrote a change review it.

Every brief states the goal, the files it owns, the smallest context it needs,
the constraints, the check that proves it is done, and the shape of its reply.
Do not send conversation history or your own conclusions to a reviewer.

## Stages

Keep a short run ledger in a scratch file: stage, status, artifacts,
decisions, and the next action. Update it at every gate so the run can resume.

1. **Plan.** State the outcome and how it will be proven. Send one or more
   `explorer` agents in parallel to map the current behavior, owners, and
   tests. If requirements are unclear, use `$clarify-requirements` for a few
   blocking questions or `$shape-idea` for an open idea. Gate: the outcome and
   its proof are concrete.
2. **Spec.** For a new boundary, contract, or state model, run `$architect`.
   Otherwise write the spec yourself: units of work, each with its files,
   behavior, and done-when check, in dependency order. Ask one `adversary` to
   challenge it. Gate: every requirement maps to a unit, and the adversary's
   supported objections are resolved.
3. **Build.** Give each unit to a `worker`, or to `luna` when it needs
   judgment. Run units in parallel only when their files are disjoint. Each
   unit must pass its check before you build on it. Integrate, run the
   repository's checks, and prove the result in the real product with
   [Feature Development](../../references/feature-development.md)'s proof step
   and the repository's `verify-<app>` skill when it has one. Gate: checks and
   proof pass.
4. **Review.** Run `$change-review` at the chosen level. Gate: supported
   findings are repaired and re-checked.
5. **PR.** Run `$publish-pr`. Gate: the pull request contains the pushed
   commit and is ready for review.
6. **Babysit.** Run `$babysit-pr` until checks pass and review feedback is
   handled. Do not merge unless the user asks.

## Report

Write updates and the final report with
[Writing style](../../references/writing-style.md). At each gate, tell the
user in one or two lines what passed and what runs next. Finish with the pull
request link and its check status, the proof, the decisions the request did not
cover with how to reverse each, and anything still unverified.
