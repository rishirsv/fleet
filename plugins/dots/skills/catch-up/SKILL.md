---
name: catch-up
description: "Summarizes work completed, current status, and decisions awaiting the user in this chat or earlier Codex and Claude sessions. Use when the user selects $catch-up or requests a work-status recap."
---

# Catch up

Tell the user where things stand and what needs them, in plain words. Choose
the scope from the request:

- **This chat** (default): everything since the last message the user wrote
  before asking. Notifications and subagent results are not their messages.
- **Earlier sessions**: "what have I been working on?", "where did I leave
  off?", a named task, or a time window.

Keep this turn read-only. Do not change code, start an app or job, or post
anything; making visuals for the reply from material you already have is fine.
Call each PR, branch, file, or agent by a name the user would recognize, never
by a label invented during the work.

## Gather this chat

Collect your own work since that message, subagent reports, and messages from
anyone else in the chat. Assume the user remembers their message and nothing
after it.

## Gather earlier sessions

Read history through [Session history](../../references/session-history.md).
Use a supplied summary instead of searching again, and read one named task
directly.

1. **Set the scope.** Identify the topic, workspace, and time window. Treat
   "recent" as seven days unless context says otherwise. Never narrow "all"
   or cross projects silently.
2. **Read the smallest useful history.** List candidates across the Codex and
   Claude stores in scope, newest first by update time, and inspect only
   matching tasks and regions. Skip this task and tasks created only for
   subagents, evaluations, or tests.
3. **Recover the facts.** Capture the goal, decisions, open work, failed
   approaches, and artifacts such as PRs, branches, plans, and reports, each
   with its task ID. When a gap remains, widen to the other agent's store or
   an authorized chat export before guessing. Use `$why` for a question about
   repository history.

## Check what is true now

Check the current state of every PR, CI run, branch, and agent you found. A
transcript says what happened, not what remains true. Say which are still
running and which you could not check. For earlier sessions, give each thread
one status: `[merged #N]`, `[open PR #N]`, `[in flight <branch>]`,
`[verified, uncommitted]`, `[reverted #N]`, `[planned, not started]`,
`[blocked]`, or `[status unverified]`. Missing access is not evidence that
work is unstarted or complete.

An action item is a decision or step only the user can take: a product choice,
an approval, an irreversible action, or access you lack. Include any still
waiting from earlier. Work you can still do yourself is not an action item.

## Write the reply

Follow [Writing style](../../references/writing-style.md) and write in plain
spoken language.

1. Open with one sentence giving the number of action items, or saying there
   are none. If nothing happened and nothing waits on the user, say so and stop.
2. Say what happened, most important first: each result and what it means for
   the user. For earlier sessions, list the threads with their status and any
   recurring problem, including a fix that shipped and was reverted. Name in
   one line any remaining work you can do yourself.
3. Give each action item a short summary: the decision, why it matters now, the
   options and what each costs, your recommendation, and what happens if the
   user does not answer. Say when you do not know a part. Link the detail when
   it exists, and write the summary so the user can decide without opening it.
4. End with the single most useful next action.

Show each action item as a before and after, side by side. For a choice, put
the current state beside each option, or the options alone when nothing exists
yet. Use screenshots or video you already captured when the change is visible;
otherwise use a table, a diff, or a diagram from
[Visual explanations](../../references/visual-explanations.md). If no visual
can be made from real material, say so. Never invent a number, never draw a
screen you did not capture, and link only artifacts that exist.

Cite session findings by agent and task ID and shared records by their source
(PR number, ticket ID, link). Remove private context before any public output.
