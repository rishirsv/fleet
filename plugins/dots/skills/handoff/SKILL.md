---
name: handoff
description: "Creates a continuation brief for the current task, branch, pull request, plan, or conversation. Use when the user asks to hand work to another task, agent, or phase; use recall to reconstruct earlier work and publish-pr to publish changes."
---

# Handoff

Create a practical continuation brief for the current task, branch, PR,
issue, plan, or conversation.

Default to an inline handoff in chat. Write a file when the user asks, the brief
is too large for chat, or the next workflow needs a saved artifact. Use the
requested path. If no path was supplied, use a clearly named temporary path.
Report the saved path.

Use a handoff at a phase boundary when the next agent should inherit the work,
not the whole discussion: research to decision, decision to implementation,
implementation to verification, one pull request to its dependent, or local
proof to release. Name the phase that ended and the next objective that can be
completed as one task.

## Context

Use the visible conversation and current workspace first: branch, dirty files,
recent commits, active plans, issue/PR links, and validation already run. Reach
for prior-session history only when it materially improves the handoff, the user
asks to continue earlier work, the work spans sessions, or the current state is
unclear, and provide the relevant facts rather than reproducing the transcript.
If a source is unavailable, note it under risks and continue.

When the next agent may run on another machine or in a fresh checkout, list the
state that exists only here: unpushed branches or commits, stashes, untracked
or scratch files, local servers or processes, and local configuration the work
depends on. The handoff is complete when the next agent would not need to ask
a question this session already answered.

Keep the facts that affect the next decisions. Keep settled decisions that
constrain future work, current state, checks whose results still apply, current
artifacts, unresolved questions, and the point where work should resume. Omit
repeated narration, raw tool logs, superseded plans, rejected alternatives that
no longer explain a constraint, and unrelated project history. Preserve a
rejected direction only when repeating it is a credible risk; label it as an
exclusion rather than retelling the debate.

## Destination

Use the smallest route the user asked for: inline (default), saved file, new
session or thread, isolated worktree, or forked conversation. Platform
thread and workspace actions happen only when explicitly requested and the
platform provides the tool.

For a fresh continuation, make the brief self-contained enough to execute
without opening the source transcript.

## Codex

For prior-session context in Codex, prefer available platform thread tools.
Use the packaged helper only when those tools are unavailable; do not scrape
`~/.codex/state_5.sqlite` or rollout files manually:

```sh
python3 <handoff-skill-dir>/scripts/handoff_context.py --latest --cwd "$PWD"
python3 <handoff-skill-dir>/scripts/handoff_context.py --thread <thread-id>
python3 <handoff-skill-dir>/scripts/handoff_context.py --query "<title or prompt text>"
```

For an explicit new-thread handoff, use `create_thread` (environment
`local` for the current checkout, `worktree` for isolation) or
`fork_thread` for a child of this thread's history, then report the created
or pending thread id with the required Codex thread directive.

## Claude Code

In Claude Code, keep the brief self-contained and based on files and paths.
Reference repo instructions such as `CLAUDE.md` or `AGENTS.md` when they exist,
but do not rely on Codex thread ids, rollout files, or Codex-only continuation
tools.

## Output

Summarize completed work, current state, decisions, and constraints; reference
artifacts by path or URL and name what changed since they were written, instead
of duplicating them; list next actions in execution order; name validation run
and still needed; call out blockers, assumptions, and risks. Identify which existing verification
remains reusable so the next agent does not repeat valid work. Use the structure
below as a guide, omitting empty or irrelevant sections. Keep unknowns that
could affect the work. Distinguish checks that passed from checks still needed:

```md
# Handoff: <task>

## Purpose
<what the next agent should accomplish>

## Current state
<what is done, partially done, or unchanged; machine-local state when it matters>

## Key decisions
<decisions already made and why>

## Scope
- In: <work the continuation owns>
- Out: <superseded or explicitly excluded work>

## Artifacts
- `<path or URL>` - <why it matters>

## Next actions
1. <concrete next step>

## Validation
- Run: <checks already run>
- Reusable evidence: <proof that still applies and under what checkout/configuration>
- Still needed: <checks/manual review still needed>

## Risks and unknowns
- <risk or assumption>
```

For a platform continuation, prepend one line: "Continue this task from the
handoff below. Start by reading the referenced files and repo instructions,
then proceed with the next actions." Leave secrets, tokens, and private keys
out of every handoff.
