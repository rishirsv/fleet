# Design docs

A design doc identifies costly mistakes before implementation. It explains
decisions that are hard to reverse, risky to misunderstand, or necessary for
people or systems to coordinate.

Contents:

- [Find the costly decisions](#find-the-costly-decisions)
- [Core shape](#core-shape)
- [How to build it](#how-to-build-it)
- [Level of detail](#level-of-detail)
- [Open issues and alternatives](#open-issues-and-alternatives)

## Find the costly decisions

Before choosing sections, ask:

- What would be painful to change after code ships?
- What assumption could force rework if it is wrong?
- What will other people or systems depend on?
- What failure would be costly, unsafe, or hard to diagnose?
- What are reviewers most likely to challenge?
- What looks easy now but locks in a data model, protocol, vendor, deployment
  topology, permission model, or user promise?

Document those areas deeply and leave easily changed choices brief or to
implementation. A database, public API, auth model, retention rule, or
migration strategy often belongs in the doc; button copy, small helpers, and
easily swapped libraries usually do not unless they create real risk.

## Core shape

Start small and add sections for the risks of the work. Omit any section that
does not change the reader's ability to review the design.

- **Title**: short, distinctive, and stable enough to reference.
- **Metadata**: only fields the repository convention supports, such as
  author, status, owner, path, and reviewers.
- **Objective**: one plain sentence saying what the project will make true.
- **Background**: the problem, relevant prior attempts, and the context a
  reviewer needs before reacting.
- **Goals and non-goals**: outcomes after delivery, and specific exclusions
  that stop scope creep and wrong review expectations.
- **Scenarios**: concrete user, system, migration, failure, or operational
  flows that reveal required behavior.
- **Proposed design**: architecture, interfaces, data model, dependencies,
  ownership, and important mechanisms.
- **How to build it**: when build order, integration, rollout, test strategy,
  or migration safety affects the design.
- **Risks and constraints**: security, privacy, reliability, legal, cost,
  compatibility, performance, staffing, timeline, or platform limits.
- **Open and resolved issues**, and **alternatives considered**.

## How to build it

Include a build plan when implementation order is part of the design: staged
rollout, migration safety, early feedback, cross-team coordination, or proof
that the design can ship without a large risky launch. Keep the build strategy
reviewers need to validate the design here; delivery order and task tracking
belong in the roadmap, issue tracker, or pull request, following the
repository's ownership model.

Useful parts are build order, integration points, interfaces to create or
change, data and migration steps, rollout and rollback, validation, and
sequencing across owners when coordination matters.

Milestones should describe a capability a user, operator, or reviewer can see,
and should test the riskiest assumptions early:

- "Serve a read-only mirror from hardcoded fixture data."
- "Load real data in a test environment with writes disabled."
- "Enable writes for internal users behind a feature flag."
- "Roll out to 5% of traffic with rollback verified."

Chores such as "create database tables" or "add tests" belong in the tracker;
the doc explains why the sequence reduces risk.

## Level of detail

Give reviewers enough to assess the design without reading the future code:
interfaces, schemas, commands, and examples that others depend on; diagrams
where they reduce ambiguity about flows, ownership, boundaries, or lifecycle;
scenarios covering failures and permission boundaries; SLOs when performance
or reliability shapes the architecture; and rationale for security, privacy,
logging, retention, and legal decisions.

Leave out implementation notes that will be stale by code review, cosmetic
choices that encode no requirement, and rejected ideas no reviewer would ask
about. Replace vague goals such as "fast" or "secure" with concrete criteria,
and label an unknown target as an open issue instead of inventing precision.

## Open issues and alternatives

Each open issue states the question, why it matters, plausible options, the
current recommendation, and the next step and owner when known. When it is
resolved, move it to resolved issues with the decision, rationale, and
follow-up implications, keeping the original question.

List alternatives reviewers are likely to ask about or that consumed real
investigation: what it was, what made it attractive, and why the design does
not choose it. The section exists to prevent repeat debate.
