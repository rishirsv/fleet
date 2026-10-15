---
name: how
description: "Explains how code, a subsystem, or a change works by tracing its source. Use for runtime flow, ownership, or a walkthrough of a commit, branch, or PR; use why for historical rationale."
---

# How

Trace the source to explain how code, a subsystem, or a change works. Match
the explanation to the reader and show how the parts work together so they
can understand or change the implementation.

## 1. Understand the question and choose the depth

Identify the scope from the conversation and repository. If it is ambiguous,
state your best interpretation and proceed so the user can redirect you.

Read [tracing.md](references/tracing.md) before exploring. For a diff, commit,
branch, pull request, or completed body of work, also read
[changes.md](references/changes.md).

Choose the exploration path:

- **Simple:** a single module, small utility, or narrow function. Explore and
  explain it directly in the current context.
- **Complex:** a subsystem spread across several files or services, a
  feature that crosses modules, or a broad architectural overview. Investigate
  the code yourself if you can follow all paths needed to answer the question.
  Add read-only explorers when they can investigate independent paths or
  when parallel work will cover more evidence or finish substantially faster.

When in doubt, investigate directly.

## 2. Trace the source

Find the real entry point. Follow its callers, callees, types, state changes,
data flow, module boundaries, and observable effects. Read the implementation
before drawing conclusions from file names.

When delegating a complex question, divide the work by parts that answer
different pieces of the question. A rate limiter might split into:

- data model and state management;
- request path and enforcement; and
- configuration, metrics, and operational controls.

Build each explorer brief from
[explorer-prompt.md](references/explorer-prompt.md), and name what the other
explorers cover.

## 3. Build one explanation

Combine your findings into one explanation. Resolve conflicting findings
before writing the answer. Combine reports in the current context unless
they are large or each require substantial analysis.
Only then use a separate explainer built from
[explainer-prompt.md](references/explainer-prompt.md), and supply `tracing.md`
and the output contract below with it. Supply
[Writing style](../../references/writing-style.md) as a resolved file path the
explainer can read, or include its contents in the prompt.

Link claims that affect the explanation to specific files and symbols.

## Output contract

Write the explanation with [Writing style](../../references/writing-style.md).

Adapt these sections to the question. Do not include an empty section merely
because it appears here.

- **Overview.** One or two paragraphs explaining what the thing is, what it
  does, and how its parts work together. The reader should know whether to keep reading.
- **Key concepts.** Brief definitions of the types, services, or abstractions
  needed to understand the rest. Include only the important ones.
- **How it works.** Walk through the trigger-to-effect flow in prose. Explain
  the order, state, data movement, and decision points. Cite files and functions
  without turning the answer into annotated source.
- **Where things live.** Give the smallest useful map of files and ownership so
  the reader knows where to start working.
- **Gotchas.** Explain the surprising behavior, hidden coupling, historical
  constraint, or failure risk a newcomer is likely to miss.

When the user asks to see, diagram, or make the explanation visual, read
[Visual explanations](../../references/visual-explanations.md) and include the
smallest useful view. Otherwise use a visual when several components interact
or data changes shape across stages and the picture makes that relationship
easier to understand. Skip it when prose already makes the flow clear.

## Delivery and completion

Return chat unless the user asks for HTML or a durable, visual, or shareable
artifact. For HTML, load the `html` skill and apply it to the finished content and
structure with this skill's `artifact-template.json`. HTML adds visual explanations by default;
provide the flows, state changes, dependencies, and evidence needed to draw
them accurately. Preserve any fixed template requirements.

The explanation is complete when it answers the question or covers the
meaningful change, links important claims to source, makes material gaps
visible, and can be understood without opening the repository.
