# Document types

Choose the closest recipe after identifying the documentation job. Repository
structure and metadata conventions come first, including required or forbidden
status, date, ownership, and frontmatter fields. Each recipe lists the usual
parts; omit any that do not help this reader.

Contents:

- [README](#readme)
- [Concept](#concept)
- [Flow doc](#flow-doc)
- [How-to](#how-to)
- [Tutorial](#tutorial)
- [Reference](#reference)
- [Runbook](#runbook)
- [Troubleshooting](#troubleshooting)
- [PRD or feature spec](#prd-or-feature-spec)
- [Design doc, ADR, or design note](#design-doc-adr-or-design-note)
- [Investigation plan](#investigation-plan)
- [Validation plan](#validation-plan)
- [Changelog and release notes](#changelog-and-release-notes)
- [Knowledge concept](#knowledge-concept)

## README

Helps a new reader decide what the project is and take the next step. Include
generated-file boundaries; link to architecture essays, roadmaps, and
exhaustive API references instead of including them.

## Concept

Explains a system or abstraction before the reader acts, including what it
does not cover. It explains rather than instructs; include examples only when
they clarify the model. Center it on a bounded why question and explain the
trade-offs behind the answer.

## Flow doc

Traces how a request, behavior, or state transition moves through existing
code, as a navigable explanation rather than a line-by-line restatement.
Include entry points and required state, the points where state is copied,
frozen, or committed, exit states, the handoff contract with adjacent flows,
and failure paths with their observable evidence.

Keep separate lifecycle or domain flows separate when combining them would hide
their boundaries; each standalone flow still states what it receives, what it
produces, and which flow owns the next step. Point to code with repo-relative
links, stable symbols, or searchable identifiers rather than local checkout
paths or line numbers alone.

## How-to

Solve a reader's task, assuming the relevant basic skills. Include decision
branches when the goal requires them; link background and lookup details.
Split independent goals into separate how-tos.

## Tutorial

Name what the learner will build. Use a safe, reproducible example with
observable progress and expected results. Keep explanations brief and link
deeper material; avoid making the learner choose among unexplained options.

## Reference

Organize lookup facts to match the interface: behavior, options, defaults,
limits, and errors. Keep advocacy and lessons elsewhere. Add a source or
generation note when the reference is derived. Cover the declared interface
without turning a focused request into a catalogue of the whole repository.

## Runbook

Mark commands with external effects and the points where a human decides
whether to continue.

## Troubleshooting

Start from symptoms or errors. Quote exact error text when available and put
the most common fix first.

## PRD or feature spec

A durable product contract: problem, target users and jobs, goals, non-goals,
user stories, prioritized requirements, acceptance criteria, success criteria,
risks, open questions, and phasing when relevant.

Without a stronger repository convention, group requirements as **P0 /
Must-have** (required to solve the core problem), **P1 / Should-have**
(important, can follow the core launch), and **P2 / Future consideration**
(out of scope now, kept as design context).

Make acceptance criteria independently testable with Given/When/Then or a
checklist covering happy and important failure paths. Define words such as
"fast" or "easy" concretely or drop them. Success criteria name the intended
outcome and, when evidence supports it, the measurement, target, and window;
label unknown metrics as hypotheses or open questions.

Gather source evidence while writing, but leave provenance, reviewed-scope,
and audit sections out of the PRD itself.

## Design doc, ADR, or design note

For a design doc, follow the design docs reference.

An ADR records one durable decision: status only when the repository uses it,
context, decision, consequences, alternatives considered, and evidence. Keep
the decision distinct from implementation steps. Call an unmade decision a
proposal or design note rather than an ADR.

## Investigation plan

An evidence-driven path to a diagnosis when several plausible causes remain:

- Symptom, affected behavior, and the facts and evidence already collected.
- Competing hypotheses, ordered by likelihood or cost to test when useful.
- For each hypothesis, supporting and contradicting evidence, the smallest
  check that separates it from the others, and the expected result either way.
- Reproduction or evidence-capture procedure.
- What establishes the root cause and what evidence would require a new
  hypothesis.
- Findings and remaining uncertainty as the work progresses.

Keep observations separate from inferences, and present an unconfirmed
hypothesis as a hypothesis.

## Validation plan

Durable agreement about which checks to run and which results are acceptable.
It defines coverage; it does not claim validation has passed.

- Subject, scope, and linked requirements or risks.
- Environments, fixtures, data, and prerequisites.
- Automated checks and the behavior each proves; manual checks only for
  behavior automation cannot reasonably establish.
- Happy paths, boundaries, failures, permissions, migrations, and rollback.
- Expected results, acceptance criteria, evidence to retain, and owners when
  coordination matters.
- Known coverage gaps and their consequences.

Tie every check to a requirement, risk, or plausible failure. A file existing
or a generic smoke check passing does not prove the required behavior.
Record actual results only after observing them.

## Changelog and release notes

A reader-facing account of changes since the last release, derived from git
history and merged PRs (`git log`, merge commits, PR titles and descriptions)
with no invented entries. Give the version, a date only when the release
artifact already uses dates, highlights grouped by reader impact, breaking
changes with migration notes, fixes, known issues, and links when useful.
Include implementation details only when they change behavior,
compatibility, or operations.

## Knowledge concept

An agent-readable unit in a Markdown corpus or OKF-style bundle: YAML
frontmatter with `type`, `title`, `description`, and optional `resource`,
`tags`, or repo-specific fields; body sections that fit the concept, such as
`# Schema`, `# Examples`, `# Steps`, `# Relationships`, `# Failure Handling`,
or `# Citations`; and bundle-relative links where a future agent should
traverse context.

When changing a bundle, preserve unknown existing frontmatter fields unless the
user asks to remove them, match index entries to added, removed, and renamed
concept files, and keep each description useful as a one-sentence search or
index snippet. Give external claims inline source links or a `# Citations`
section when source authority matters.
