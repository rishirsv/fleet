---
name: catch-up
description: "Catches the user up on everything in this chat since their last message, in plain words, and turns each decision waiting on them into a short summary they can act on. Use only when the user selects `$catch-up`; use recall for earlier sessions."
---

# Catch up

Catch the user up on this chat since the last message they wrote before
`$catch-up`. Notifications and subagent results are not their messages. Assume
they remember that message and nothing after it. Call each PR, branch, file, or
agent by a name they would recognize, never by a label invented during the work.

Use [Recall](../recall/SKILL.md) instead when the user wants work from earlier
sessions.

## Gather what changed

Keep this turn read-only. Do not change code, start an app or job, or post
anything; making visuals for the reply from material you already have is fine.

Collect your own work since that message, subagent reports, and messages from
anyone else in the chat. Check the current state of each PR, CI run, or agent
the chat touched. Say which are still running and which you could not check.

An action item is a decision or step only the user can take: a product choice,
an approval, an irreversible action, or access you lack. Include any still
waiting from before their last message. Work you can still do yourself is not
an action item.

## Write the reply

Follow [Writing style](../../references/writing-style.md) and write in plain
spoken language.

1. Open with one sentence giving the number of action items, or saying there
   are none. If nothing happened and nothing waits on the user, say so and stop.
2. Say what happened, most important first: each result and what it means for
   the user. Skip steps that changed nothing. Name in one line any remaining
   work you can do yourself.
3. Give each action item a short summary: the decision, why it matters now, the
   options and what each costs, your recommendation, and what happens if the
   user does not answer. Say when you do not know a part. Link the detail when
   it exists, and write the summary so the user can decide without opening it.

Show each action item as a before and after, side by side. For a choice, put
the current state beside each option, or the options alone when nothing exists
yet. Use screenshots or video you already captured when the change is visible;
otherwise use a table, a diff, or a diagram from
[Visual explanations](../../references/visual-explanations.md). If no visual
can be made from real material, say so. Never invent a number, never draw a
screen you did not capture, and link only artifacts that exist.
