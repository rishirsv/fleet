# Document types

Choose the closest recipe after identifying the documentation job. Repository
structure and metadata conventions come first, including required or forbidden
status, date, ownership, and frontmatter fields. Each recipe lists the usual
parts; omit any that do not help this reader.

Contents:

- [README](#readme)
- [Concept](#concept)
- [Flow doc](#flow-doc)
- [How-to and tutorial](#how-to-and-tutorial)
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

An introduction that helps a new reader decide what the project is and take the
next useful step: purpose and scope, the most common workflow, a source map,
expected contributor commands, current constraints, and generated-file
boundaries. Link to deeper docs instead of repeating them; architecture essays,
roadmaps, and exhaustive API references belong elsewhere.

## Concept

Explains a system, model, or abstraction before the reader acts: what it is,
why it exists, its vocabulary, how the parts relate, what it does not cover,
and links to tasks or decisions. A concept doc explains rather than instructs;
include examples only when they clarify the model.

## Flow doc

Traces how a request, behavior, or state transition moves through existing
code, as a navigable explanation rather than a line-by-line restatement.

- Scope, entry points, and required state at entry.
- A high-level diagram when it clarifies control or ownership boundaries,
  chosen with the shared visual explanations guidance.
- The execution trace through important components, branches, and state
  changes, including points where state is copied, frozen, or committed.
- Exit states, outputs, and the handoff contract with adjacent flows.
- Failure paths and observable evidence such as logs, metrics, or events.

Keep separate lifecycle or domain flows separate when combining them would hide
their boundaries; each standalone flow still states what it receives, what it
produces, and which flow owns the next step. Point to code with repo-relative
links, stable symbols, or searchable identifiers rather than local checkout
paths or line numbers alone.

## How-to and tutorial

A how-to reaches one concrete outcome by a flexible path: goal,
prerequisites, steps, how to confirm the result, and rollback or
troubleshooting when failure is common. Split independent goals into separate
how-tos.

A tutorial teaches by completing a safe path, with expected observations at
each step, cleanup, and next steps. Prefer reliable toy inputs over
production-specific examples, and keep lookup material out of it.

## Reference

Lookup material such as commands, config, schemas, API fields, events, or
environment variables. Optimize for scanning and exactness: stable tables or
definition lists with names, types, defaults, and required status, plus a
source or generation note when the reference is derived. Prefer generated
references, or a link to the defining source, over a hand-copied inventory.

## Runbook

An operational procedure: trigger, preconditions and access, commands, expected
healthy output, failure handling and escalation, and completion criteria. Mark
commands with external effects and the points where a human decides whether
to continue.

## Troubleshooting

Starts from symptoms, errors, or failed checks, then gives likely causes,
diagnosis, fixes, confirmation, and escalation. Quote exact error text when
available and put the most common fix first.

## PRD or feature spec

A durable product contract: problem, target users and jobs, goals, non-goals,
user stories, prioritized requirements, acceptance criteria, success criteria,
risks, open questions, and phasing when relevant.

Write user stories as "As a [user type], I want [capability] so that
[benefit]" when that format helps. Keep the user type specific, describe the
capability rather than a widget or technical solution, state the value, and
give each story one capability. Cover important edge, error, empty, and
boundary states. Record internal team work as requirements or technical notes
rather than user stories.

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

Write a design doc when an engineering change needs alignment before
implementation, especially when choices are expensive to reverse, several
people or systems coordinate, requirements are ambiguous, or the work carries
security, privacy, data, reliability, compatibility, cost, or maintenance risk.
Its guidance is in the design docs reference.

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
