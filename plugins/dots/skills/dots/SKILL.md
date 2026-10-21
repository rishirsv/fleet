---
name: dots
description: "Routes a request to the owning Dots skill, shared reference, or Feature Development workflow. Use only when the user explicitly invokes Dots, $dots, or Dots Feature Development."
---

# Dots

Route the request to the smallest Dots workflow that owns it. Dots selects
and loads the skill responsible for the work; it does not repeat or replace
its instructions.

## Route the task

- When one focused skill clearly matches, load it and follow it directly.
- When several skills apply, choose one primary owner and add only the
  supporting skills needed for distinct parts of the work.
- Read each selected skill or reference before acting on it. Preserve its
  authorization, output, validation, and completion rules.
- Do not turn the skill map into a checklist. Skip routes that do not change
  the work.
- User instructions take precedence over Dots skill guidance. When a skill
  causes a pause or a divergence from the user's intent, name its `SKILL.md`,
  quote the instruction, and separate what the skill explicitly requires from
  your interpretation of it.

## Non-negotiables

The Principles section below grounds every trigger. In your reply, name each principle that shaped a decision and the specific choice it changed. Cite only principles whose linked guidance you read this session.

Remaining triggers:

- Nontrivial change, architecture decision, or "are we sure?" → the [How](../how/SKILL.md) skill.
- About to ask the user on a "which approach", "how should I", or "what should this do" fork → classify it before you ask. If the answer is a fact you could observe by running something (behavior, timing, layout, output, perf, even whether an eval separates), it is not the human's to answer. Sketch it via the [Prototype](../prototype/SKILL.md) skill and let the result decide. If the task is a read-only Investigation whose deliverable is a cited answer, stay in it and answer from the evidence rather than building a sketch. Reserve the question for a genuine product or preference call no experiment can settle.
- Any code → name the data shape first, and choose its organizing structure per [Model the Domain](../../references/engineering-principles.md#model-the-domain).
- Code crossing a function boundary → the [Architect](../architect/SKILL.md) skill before implementing. The skill owns when a local correction suffices and when independent design exploration is needed.
- Contested design → the [Change Review](../change-review/SKILL.md) skill before shipping.
- Any prose surface, your reply to the user included → [Writing style](../../references/writing-style.md). Agent-facing prose also follows the environment's default skill creator.
- Docs, RFCs, readmes, PR descriptions, or commit messages → the [Repo Docs](../repo-docs/SKILL.md) skill for repository documents, and [Writing style](../../references/writing-style.md) for PR descriptions or commit messages.
- Shipping UI / IDE / CLI → the repository's verification skill, existing harness, or available app-control tool. For bug fixes, reproduce first on the same surface yourself. Hand to the user only under the narrow [Bug fix](../../playbooks/bug-fix.md) step 1 exception.
- Bugbot or the agentic security review commented → skeptical posture. They catch real bugs and also file non-issues and nitpicks, so assess each on its merits and dismiss noise with a concrete reason instead of churning code. Use [Change Review](../change-review/SKILL.md) for a review and [Babysit PR](../babysit-pr/SKILL.md) for an authorized monitoring run.

The selected owner keeps its scope, review budget, and completion rules. Delegation uses the host's available agents, permissions, and configured model policy. Commit, publish, merge, send messages, or schedule future work only within the user's authorization and repository instructions.

## Follow the current task

Continue the selected workflow on follow-ups such as "do it" or "continue,"
within the outcome and permissions already established. When the user changes
the outcome or switches between investigation, planning, implementation, or
review, select the owner again and apply the new stopping point. Carry forward
relevant facts and settled constraints, not the previous workflow's remaining
actions. Answer an interim question or status request, then resume the active
task unless the user changes or stops it. "New task" makes a switch explicit
but is not required. Ask only when those readings would lead to materially
different work.

## Develop software

For a material feature, bug fix, refactor, measured performance change,
behavior-changing configuration, or implementation plan, read and follow
[Feature Development](../../references/feature-development.md) as the primary
workflow. It routes into focused skills as its phases require.
Use `$agent-workflow` instead when the user wants the whole plan-to-PR flow
run with delegated agents.

## Playbooks

Match the task to a playbook below and open its full steps before acting. For a multi-step task, open a todo list whose first items are the matched playbook's steps, copied in verbatim, before any task-specific todos. A step you choose not to do stays in the list with a one-line `skip: <reason>`. An existing task record can hold these steps; do not create a second checklist.

- **[Investigation](../how/SKILL.md).** Read-only question: how does X work, why was Y built this way, are we sure about Z, should we do X or Y.
- **[Bug fix](../../playbooks/bug-fix.md).** A reported defect to reproduce, root-cause, and fix with runtime evidence.
- **[Perf issue](../../playbooks/performance.md).** A measured slowness to trace and improve against a baseline.
- **[Feature](../../references/feature-development.md).** New or changed behavior, built from a named data shape.
- **[Refactoring](../../playbooks/refactoring.md).** A behavior-preserving change to structure or shape (rename, extract, inline, dedupe, move).
- **[Prototype](../prototype/SKILL.md).** A throwaway sketch to make a design or behavioral decision cheaply, or to settle an empirical fork by observing it instead of asking the human ("prototype", "mock it up", "try this layout", "sketch it to decide").
- **[Authoring or modifying a skill](../skill-standards/SKILL.md).** Writing or editing a SKILL.md.
- **[Eval](../../playbooks/eval.md).** Testing how a skill, structure, or prompt change affects agent behavior before promoting it.
- **[Babysit](../babysit-pr/SKILL.md).** Driving a PR or a stack to merge-ready: conflicts, review threads, CI.
- **[Multi-phase or multi-PR plan](../../references/feature-development.md#stop-at-a-planning-handoff-when-requested).** Work that spans phases or stacked PRs.
- **[Opening a PR](../publish-pr/SKILL.md).** Open a ready PR from small ordered commits with a conventional commits title and a briefing-style body.

Investigation requests are read-only. They produce a cited explanation or a recommendation, not a code change. For motivation questions, also route through the [Why](../why/SKILL.md) skill.

Bug fix, Perf issue, Feature, and Refactoring run within [Feature Development](../../references/feature-development.md). It owns scope, planning-only stops, review, and completion; the selected playbook owns the technical sequence. Eval ends at a recommendation for whether to promote the variant. Babysit applies when the user requests monitoring; a one-time PR-status question remains a one-time check. Opening a PR applies only when publication is requested.

Use [Task-specific workflow](../../playbooks/task-specific-workflow.md) whenever no bundled playbook fits and the task needs dependent experiments or changes. It designs a bespoke, rigorous playbook for the task. Use [Handoff](../handoff/SKILL.md) for a continuation brief or an explicit pause, and its session-history guidance when resuming prior work.

## Choose the focused owner

Each skill's description defines its boundary. Choose within these groups:

- Design and structure: `$architect`, `$architecture-review`, `$prototype`
- Review and publishing: `$change-review`, `$publish-pr`, `$babysit-pr`
- Effects beyond a named diff: `$blast-radius`
- Reusable formal checks for a named invariant: `$formal-verification-skill`.
  This does not add formal tooling to ordinary implementation or app verification.
- Explanation and documentation: [Teach](../teach/SKILL.md), `$how`, `$why`, `$repo-docs`
- Documents: `$html` for browser-openable documents; `$editorial-pages` for
  native ChatGPT Page explainers. Product interfaces use `$design` and `$design-review`
  from the separate Design plugin when installed. If unavailable, complete the
  task directly with existing product sources and Dots visual-proof guidance.
- Agent work: `$apply-ambition`, `$handoff`, `$meta-prompt`, `$skill-standards`

The user-controlled modes `$ask-model`, `$clarify-requirements`,
`$shape-idea`, `$explain-simply`, `$catch-up`, `$self-improve`,
`$usage-insights`, and `$verification-skill`
remain explicit. Load them only when the user selects that mode. Their
descriptions define the exact boundary.

## Load shared references by need

- Read [Hard-cut policy](../../references/hard-cut-policy.md) when replacing a
  schema, contract, persisted shape, route, configuration, value set, or
  architecture, unless the selected skill already loads it.
- Read [Duplicate ownership](../../references/duplicate-ownership.md) when a
  change creates or removes copied policy, competing sources of truth, or
  normalization in several layers, unless the selected skill already loads it.
- Load other shared references, such as writing style, visual explanations, and
  session history, through the skill that links them.

## Principles

Read the linked guidance in full for any principle you apply. Each entry names when it applies. Existing skills and shared references own the full guidance.

**Core**

- **[Laziness Protocol](../../references/engineering-principles.md#laziness-protocol).** Refactoring, sizing a diff, or tempted to add abstractions, layers, or signal threading. Bias to deletion and the smallest change that solves the problem.
- **[Foundational Thinking](../../references/engineering-principles.md#foundational-thinking).** Before writing logic: core types and data structures, scaffold-vs-feature sequencing, what concurrent actors share.
- **[Redesign from First Principles](../architect/SKILL.md#phase-e-scrap-when-the-architecture-is-wrong).** Integrating a new requirement into an existing design. Redesign as if it had been foundational from day one.
- **[Attack the Premise](../../references/engineering-principles.md#attack-the-premise).** Two or more fixes that share one premise have failed the same gate. Write the premise down and test it directly before you write another fix that assumes it.
- **[Subtract Before You Add](../../references/engineering-principles.md#subtract-before-you-add).** Sequencing an addition, refactor, or rewrite. Remove dead weight first, then build on the simpler base.
- **[Minimize Reader Load](../../references/engineering-principles.md#minimize-reader-load).** Reviewing or shaping code that's hard to trace. Count layers and hidden state, collapse one-caller wrappers, shrink mutable scope.
- **[Outcome-Oriented Execution](../../references/engineering-principles.md#outcome-oriented-execution).** Planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture, don't preserve throwaway compatibility states.
- **[Experience First](../../references/engineering-principles.md#experience-first).** Product, UX, or feature-scope tradeoffs. Choose user delight over implementation convenience.
- **[Exhaust the Design Space](../prototype/SKILL.md#choose-the-smallest-experiment-that-tests-the-choice).** A novel interaction or architectural decision with no precedent. Build 2-3 competing prototypes and compare before committing.
- **[Build the Lever](../../references/engineering-principles.md#build-the-lever).** Any non-trivial work. Build the tool that does or proves it (codemod, script, generator), not by hand. The tool is the artifact a reviewer reruns.

**Architecture**

- **[Model the Domain](../../references/engineering-principles.md#model-the-domain).** Writing stateful logic, or code that branches a lot or repeats a shape assumption across files. Encode the domain in a structure (state machine, typed model, table or registry, reducer, boundary, the right collection) instead of scattered conditionals.
- **[Boundary Discipline](../../references/engineering-principles.md#boundary-discipline).** Wiring validation, error handling, or framework adapters. Guards at system boundaries, trust internal types, keep business logic pure.
- **[Type System Discipline](../../references/engineering-principles.md#type-system-discipline).** Designing types or a signature in any typed language. Make illegal states unrepresentable, brand primitives, parse external data at boundaries.
- **[Make Operations Idempotent](../../references/engineering-principles.md#make-operations-idempotent).** Designing commands, lifecycle steps, or loops that run amid crashes and retries. Converge to the same end state.
- **[Migrate Callers Then Delete Legacy APIs](../../references/hard-cut-policy.md).** Introducing a new internal API while old callers exist. Migrate and delete in one wave.
- **[Separate Before Serializing Shared State](../../references/engineering-principles.md#separate-before-serializing-shared-state).** Concurrent actors might write the same file, branch, key, or object. Eliminate the sharing first.

**Verification**

- **[Prove It Works](../../references/engineering-principles.md#prove-it-works).** After a task, before declaring done. Verify against the real artifact, not a proxy or "it compiles".
- **[Fix Root Causes](../../references/engineering-principles.md#fix-root-causes).** Debugging. Trace each symptom back to the first place the system went wrong and fix it there. A guard is a fix only when the state it handles is legitimate.
- **[Sequence Work into Verifiable Units](../../references/sequence-verifiable-units.md).** Multi-step work (sweeps, migrations, runs of similar edits) and how you stack commits and PRs. Break work into small units that each end in a check, verify each before the next, and order delivery so the sequence proves itself.
- **[Test Behavior, Not Implementation](../../references/test-consolidation.md#test-behavior-not-implementation).** Writing, changing, or keeping a test. Assert what the code's users can observe, so the test fails when that behavior breaks and keeps passing when only the internals change.

**Delegation**

- **[Guard the Context Window](../../references/engineering-principles.md#guard-the-context-window).** Context fills up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents, keep summaries in the main thread.
- **[Never Block on the Human](../../references/engineering-principles.md#never-block-on-the-human).** Tempted to ask "should I do X?" on reversible work. Proceed, present the result, let the human course-correct.

**Meta**

- **[Encode Lessons in Structure](../self-improve/references/enforcement.md).** You catch yourself writing the same instruction a second time. Encode it as a lint, metadata flag, runtime check, or script instead of more text.
