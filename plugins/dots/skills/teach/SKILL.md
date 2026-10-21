---
name: teach
description: "Teaches a concept, change, or subsystem at the reader's pace, connecting what it is, how it works, and why. Use when the user wants to understand an idea beyond a summary; use how for a source walkthrough and why for historical investigation alone."
---

# Teach

Explain the idea so the reader can reason about it. Infer their purpose and
starting knowledge from the conversation. Put depth where their question is,
skip what they already understand, and keep teaching read-only unless they
also ask for changes.

## Ground the explanation

For code or a concrete implementation, orient yourself in the source, then
read and apply [How](../how/SKILL.md) for the mechanism. When the explanation
needs historical rationale, read and apply [Why](../why/SKILL.md), starting
with its focused investigation. Use both when the question needs both, and
reuse their findings rather than repeating the investigation.

For a general concept, teach it directly with a concrete example. Do not
invent a repository or historical intent to make the explanation fit.
Distinguish what a design makes possible from why its authors chose it.
Preserve Why's evidence labels, confidence language, competing explanations,
and material gaps when weaving its findings into the lesson. Link important
implementation claims to the source that supports them.

## Build understanding

Start with the smallest complete answer: name the thing in ordinary language,
explain the problem it solves, and connect it to the reader's case. Develop
that account through a concrete example of what happens and why. For a change,
follow the same example before and after. Introduce technical names when the
reader has the idea they name; a list of functions is not an explanation.

Let the conversation set the pace. In an interactive exchange, give a useful
first layer and leave room for the reader to steer deeper. Avoid quizzes,
requests to repeat the lesson, or announced pauses unless the user asks for
that teaching style. For a one-shot answer or a request for a full explanation,
cover the requested scope without withholding essential details for follow-up.

Show the relevant code, a worked example, or a diagram when it makes the
mechanism clearer. Build a complex picture in stages when that helps the
reader follow it, keeping the same example and names throughout. If an
available visualization skill would make relationships or changing behavior
easier to explore, read and apply it. Visualization is optional: without it,
use prose, a small text or Mermaid diagram, or a worked example. A simple
point needs no figure.

Use plain, spoken language and concrete mechanisms. Keep useful detail and
uncertainty while cutting filler, stock framing, and unnecessary jargon.
Return the explanation itself, with enough context to understand it without
opening the sources. Offer a next thread only when it helps the reader.
