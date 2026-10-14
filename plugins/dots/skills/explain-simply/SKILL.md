---
name: explain-simply
description: "Gives a plain-language explanation of a subject, or of the previous answer, using familiar examples. Use only when the user selects `$explain-simply`; use how for a source-traced explanation of code."
---

# Explain simply

Explain the named subject or, when none is named, the previous answer. Ask what
to explain only when neither is clear.

Use plain language that does not require specialist knowledge. Give the
background needed to answer the question without restarting the whole subject.
Lead with the answer, then explain the relevant mechanism or distinction and
provide the context needed to understand it.

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

Read the shared [writing style](../../references/writing-style.md) only for a
substantial or writing-heavy explanation.

Work from the code and context already available. Do not start a repository
investigation, review code, or create an artifact.
The user can select `$how` when they want a rigorous, source-traced
explanation of code, a system, or a change.

For a diagram, or when the user asks to see or visualize the idea, use only the
inline forms in [Visual explanations](../../references/visual-explanations.md).
