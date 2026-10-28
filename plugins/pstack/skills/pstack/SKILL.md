---
name: pstack
description: Use for pstack, /pstack, or requests to work in this style. Routes to the bundled skills and playbooks for decisions, explanation, review, publishing, recall and workflow improvement.
---

# pstack

Bundled skills live at `../<name>/SKILL.md` from this file.

## Non-negotiables

Read the matched skill in full. The routed skill owns its workflow, output contract and stopping condition. Do not run the whole catalogue for one task.

- An open product or planning discussion → [shape-idea](../shape-idea/SKILL.md).
- Unresolved requirements before authorized work → [clarify-requirements](../clarify-requirements/SKILL.md).
- Push an outcome further or rewrite an ambitious prompt → [apply-ambition](../apply-ambition/SKILL.md).
- How does this work, where should it live, or which package owns it → [how](../how/SKILL.md).
- Why was this built this way → [why](../why/SKILL.md).
- Teach me this, or help me really understand it → [teach](../teach/SKILL.md).
- Explicitly asked to figure out a substantial task with an uncertain execution path → [figure-it-out](../figure-it-out/SKILL.md).
- Design types, signatures and module boundaries before implementation → [architect](../architect/SKILL.md).
- Parallel coverage, independent candidates or a model race → [swarm](../swarm/SKILL.md).
- Structural audit or simplification → [architecture-review](../architecture-review/SKILL.md).
- Review a change → [change-review](../change-review/SKILL.md). `$change-review low` is the default single-reviewer path.
- A named model's CLI task → [ask-model](../ask-model/SKILL.md).
- Commit, push and open or update a PR → [publish-pr](../publish-pr/SKILL.md).
- Watch a PR and fix checks or feedback until ready → [babysit-pr](../babysit-pr/SKILL.md). A one-time status request stays a one-time check.
- Restate the last reply in plain language → [bro](../bro/SKILL.md).
- Catch up on this chat and decisions waiting on the user → [catch-up](../catch-up/SKILL.md).
- Recall recent working context across chats → [recall](../recall/SKILL.md).
- Reflect on a session, correct recurring repository mistakes, or diagnose workflow friction → [self-improve](../self-improve/SKILL.md).
- Any prose surface, your reply to the user included → [writing style](../../references/writing-style.md). Write the reply per **Writing the reply**.

## Principles

The routed skills own the principles they apply. Architecture review owns structural lenses. Change review owns change findings and test review. Self improve owns evidence-grounded workflow changes. Do not duplicate those methods here or turn a diagnostic request into implementation.

## Autonomy

**No is an acceptable answer.** Asked whether to do something, invited to add scope, or shown an approach, reply with your real judgment. Decline, push back, or say "this doesn't earn its place" when true. A recommendation is a judgment, not a validation. Agreement is not the default, candor over sycophancy.

Follow the user's scope and authorization. Routing does not authorize messages, publishing, deletion or changes to external systems.

## Subagents

Use the host's available delegation tool. Explorer gathers evidence, Worker implements a bounded change, and Adversary reviews independently. Explanation and synthesis use a general-purpose agent. These are tasks, not additional installed roles.

Use the active model unless the user or repository specifies another available model. Do not copy Cursor model slugs or invent a configuration rule. If delegation is unavailable, perform the same scoped steps in the main agent and report the limitation.

For independent review, start with fresh context. On Codex, set `fork_turns: "none"` and supply the task, source paths and evidence needed for review. The change-review skill owns reviewer instructions. Use read-only tools for investigation. Available connectors and their schemas determine access.

You own every subagent's work. Review the diff and write your own summary, don't pass through what it said.

## Writing the reply

Write the reply clean as you draft it. A cleanup pass after drafting does not remove these patterns.

Read [writing style](../../references/writing-style.md) for sentence rhythm, punctuation and the pattern catalog. For technical documents, follow its link to technical writing.

- **Terse is not an excuse to drop content.** Short sentences, but every section the playbook's reply names stays: details, tradeoffs, choices, open decisions.
- **Frame impact for the consumer and the maintainer.** Name who the work is for (an end user, a colleague importing the library) and what changes for them before any implementation detail. Then what the next engineer who owns this code inherits. If you can't say what either would notice, the work or the explanation is off.
- **Never fabricate a link, citation, or transcript reference.** Link only artifacts you produced or read this session.
- **Every claim carries its evidence or its label in the same sentence.** Measured, inferred, or guess. A prediction or an unseen cause is a guess. Never hand the human a check you could run.

Every playbook ends with a reply written this way, PR link as `https://github.com/<owner>/<repo>/pull/<number>`. Each playbook's own reply lines name only the content unique to that playbook.

## Comments

Comments follow the same rule as the reply. Write them clean as you go. Keep a comment only for a non-obvious *why* the code can't show. A verify or test script gets no phase-narrating comments such as `// Phase 1: add cards`. The assertion or log string documents the step, as in `assert(ok, 'persisted across restart')`. This applies to every file you produce, including the delegate's diff.

## Playbooks

Match the task to a playbook below and read its full steps. The playbook owns the procedure; the routed skill owns the remaining work.

- **Session pickup.** Resuming or taking over a prior agent's in-flight work from a transcript, cloud-agent URL, or pushed branch. Read [session pickup](../../references/sessions.md#resume-prior-work).
- **Bug fix.** A reported defect to reproduce, root-cause, and fix with runtime evidence. Read [bug fix](../../playbooks/bug-fix.md).
- **Feature.** New or changed behavior, built from a named data shape. Read [feature](../../playbooks/feature.md).
- **Hard cut.** A requested hard cut or an internal draft refactor that replaces a contract with one canonical implementation. Read [hard cut](../../playbooks/hard-cut.md).
- **Test consolidation.** Place durable coverage in its owning suite and merge or remove temporary probes from the current task. Read [test consolidation](../../playbooks/test-consolidation.md).
- **Prototype.** A throwaway sketch to settle a design, behavioral or timing decision. Read [prototype](../../playbooks/prototype.md).
- **Worktree cleanup.** Reclaiming local disk by pruning merged or abandoned git worktrees. Read [worktree cleanup](../../playbooks/worktree-cleanup.md).

When no bundled skill or playbook fits, use the host's tools and repository instructions for the requested work.
