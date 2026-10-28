# pstack

Focused operations for decisions, independent review, publishing and workflow
improvement in Codex and Claude Code. The `pstack` router selects a matching
skill or playbook. Ordinary development uses the host's tools and repository instructions.

| Skill | Use for |
|---|---|
| pstack | Route to the matching bundled skill or playbook |
| Figure It Out | Design and execute a workflow for substantial uncertain work |
| Architect | Compare interface designs and implement the chosen sketch when requested |
| Swarm | Coordinate independent parallel coverage or candidates |
| How | Explain architecture, ownership and runtime flow |
| Why | Investigate design rationale with cited evidence |
| Teach | Explain what something is, how it works and why |
| Explain | Understand a concept or decision from the conversation, including how and why |
| Catch-up | Explain changes in this chat and decisions waiting on the user |
| Recall | Reconstruct recent working context |
| Shape Idea | An open product or planning discussion |
| Clarify Requirements | Resolve ambiguities before authorized work |
| Apply Ambition | Improve an outcome without inflating scope |
| Architecture Review | Structural audits and simplification |
| Change Review | A pinned independent review and in-scope repairs |
| Ask Model | A named model's CLI task with explicit ownership |
| Publish PR | Commit, push and publish the requested work |
| Babysit PR | Monitor and repair until a PR is ready |
| Self Improve | Session reflection, recurring repository corrections, workflow diagnosis and usage |

Explorer, Worker and Adversary are optional roles for bounded independent work.
The parent keeps connected reasoning and integration. Codex reviewers explicitly
start with `fork_turns: "none"`.

Artifact and verification authoring are preserved as optional source packages
in Fleet's `wip/` area, outside pstack discovery and default installation. Local
source changes do not publish cloud releases or refresh installed caches.

This is Rishi’s plugin, renamed from Dots. It is maintained separately from
Cursor’s pstack; upstream methods are adapted for the available Codex and Claude tools.

Shared references own [writing style](references/writing-style.md),
[sessions](references/sessions.md). The router also exposes
[worktree cleanup](playbooks/worktree-cleanup.md).

Implementation playbooks cover [features](playbooks/feature.md),
[bug fixes](playbooks/bug-fix.md) and [prototypes](playbooks/prototype.md).
