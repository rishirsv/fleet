---
name: explain-simply
description: "Explains a subject or the previous answer in plain language with familiar examples. Use when the user selects $explain-simply; use how for an explanation traced through source code."
---

# Explain simply

Explain the named subject or, when none is named, the previous answer. Ask what
to explain only when neither is clear.

The reader is busy and may remember none of this session. Restore just enough
context for someone returning from another task. Make the explanation compelling
by making the consequence clear. Name the actual feature, decision, or record
before referring to it as "this" or "it". Calibrate to the knowledge the user
has demonstrated; avoid jargon the agent invented unless the user understands it.

Use plain language that does not require specialist knowledge. Start with a
short takeaway title, ideally 3–7 familiar words, that states what the reader
should understand. Lead with the answer, then explain the relevant mechanism or
distinction, why it matters, and any useful decision or action. Give the
background needed without restarting the whole subject.

Use a few plain sentences for a simple idea and a few bullets when a complex
idea needs them. Treat about 120 words per distinct topic as a rough guide, not
a limit. Let the subject and requested coverage determine the length. Keep
uncertainty next to the claim; preserve consequential limits, stored-data
changes, and the user's requested coverage.

If the user asks for several PRs or tasks, cover them all. If they ask to decide
one at a time, explain the first item and ask for that decision before advancing.
An explicit explanation request is already a reason to explain.

Explain the idea in familiar words. Describe the behavior before naming
technical terms. Use an example, analogy, comparison, or compact text diagram
only when it makes the answer clearer or shorter. If the previous answer was
unclear, explain the missing idea with a different example or comparison.

For code-related subjects, start with the problem. Introduce the important
entities and what they represent. Explain who owns each responsibility, how the
entities relate, and how they behave. Use a concrete example, and an inline
diagram only when it makes the answer clearer. Use the same example throughout
the explanation. For diffs, show the same scenario before and after, and name
every change to stored data, a schema, or a contract other code depends on. Use
short pseudocode when order or timing is the point.

Correct any misconception the context shows. Include a next action only when
useful.

Write the explanation with [Writing style](../../references/writing-style.md).

Work from the code and context already available. Do not start a repository
investigation, review code, or create an artifact.
The user can select `$how` when they want a rigorous, source-traced
explanation of code, a system, or a change.

For a diagram, or when the user asks to see or visualize the idea, use only the
inline forms in [Visual explanations](../../references/visual-explanations.md).
