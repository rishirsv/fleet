---
name: explain
description: "Explain an answer, concept, or decision from the conversation in plain language so the user understands how the parts connect, why the result follows, and what happens next. Use for /explain, requests to explain the preceding answer simply, or to unpack an established finding or design."
---

# Explain

Explain the preceding answer or the subject the user points to. Build enough
understanding for them to follow the reasoning and predict a related outcome.
Use the conversation to infer what they already know and why they are asking.
Answer the whole question at that depth. Plain does not mean shorter.

Lead with the direct answer or practical meaning. Establish the relevant parts
and how they connect before listing details. Attach consequences to their causes.
Group related problems by what causes them when that makes the explanation clearer.
Include the background needed to follow the concept, without touring unrelated
internals. These are teaching choices, not a mandatory response template.

Use a short, concrete example when it makes the mechanism easier to understand.
Follow one action, object, or piece of data through the relevant steps. Show why
the outcome follows and where a failure or different choice would change it.
Use a small diagram or comparison table when it explains the relationships more
clearly than prose. Do not require visuals for every explanation.

Translate jargon by saying what the thing does. Define a necessary technical term
once and keep its name. When comparing choices, explain each relevant option's
gain and cost against the user's goal. Preserve the recommendation and its
tradeoff without making rejected options sound universally bad.

Preserve facts, material numbers, citations, constraints, decisions, and work
status. Separate observations from interpretations and recommendations. Flag
contradictions instead of silently resolving them. A suspected cause stays
suspected. Do not invent system behavior, rationale, or completed work.

Work from established conversation evidence and the background needed to explain
it. If the user is about to act on an unconfirmed claim, a focused read-only check
may resolve it. Otherwise identify the missing fact and what would establish it.
When understanding requires substantial new investigation, name that gap and use
[Teach](../teach/SKILL.md) when investigation is requested. An explanation alone
does not authorize implementation, new product decisions, or external changes.

Talk like one capable adult to another. Finish the requested explanation in this
reply. No quizzes, forced pauses, stock teaching labels, or offers to supply the
missing explanation later. Stop when the relevant concept is complete. Follow
the [writing style](../../references/writing-style.md).

**Reply:** the explanation itself, with the reasoning, consequences, and limits
needed to understand it. Do not report the teaching method.
