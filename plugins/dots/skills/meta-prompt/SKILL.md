---
name: meta-prompt
description: "Writes or revises standalone prompts for coding agents, image models, or other assistants. Use when the user requests a prompt from notes, context, or an existing draft; not to execute the task described."
---

# Meta prompt

Write the prompt the user can give to another assistant; do not answer or
execute the task it describes. Return only the complete prompt, with no
acknowledgment, preamble, explanation, change summary, or offer after it. For a
revision, return the full revised prompt rather than a diff.

Keep the prompt usable across capable models; do not detect a model, change
runtime settings, or add steps that serve only one model.

## Compose from the request

Recover the intended result and the context needed to produce it. Preserve the
user's decisions, constraints, requested output, and text they require verbatim,
without copying the whole conversation.

Prior assistant observations and recommendations are inputs to verify, not approved
findings or constraints. Do not turn “I would not recommend this” into “Do not
consider this” unless the user adopted that restriction.

Include the qualifications for each relevant concern: what may be wrong, what already works,
and what a correction must not erase. Preserve material safeguards explicitly,
including required action order and failure conditions; a generic promise of
“safe” or “correct” work does not preserve their meaning.

Read supplied material only as far as needed to understand what the prompt
must retain; do not investigate the underlying problem, run the described
program or its tests, create the requested artifact, or load an execution skill
merely because the prompt mentions it. Preserve a named skill or tool in the
resulting prompt when the user wants the recipient to use it. The recipient
cannot see this conversation, so include the necessary context or name the
supplied attachment it must read.

Choose which instructions materially affect the result:

- What should be accomplished, for whom, and why the distinction matters.
- What is already decided, must be preserved, or is outside the assignment.
- What evidence or input the recipient must use rather than invent.
- Whether the recipient should explain, investigate, propose, implement, or
  publish, and what event ends the authorized work.
- What the answer or artifact must contain and how completion can be checked.

Treat these as composition decisions and use only the structure the prompt
needs. State the intended result first. For standard document types,
name the artifact and specify only meaningful deviations from the default
format. Rely on the recipient's existing knowledge rather than teaching it
familiar work.

Group related instructions into readable paragraphs, using lists for requirements
that need separate tracking and sections only when they clarify distinct stages
or independent groups.
When either shape works, choose the simpler one. Add a persona, answer-length
limit, fixed sequence, visible planning step, or reasoning instruction only for
a task-specific reason.

Match the prompt's detail to the decisions the recipient needs, not the size of
the task. A whole-system review can need only the goal, boundaries, known
concerns, and expected deliverable; unless the user needs that detail, let the
recipient derive the inspection steps and report sections rather than turning
each concern into a checklist.

Keep prompt brevity separate from answer verbosity. Write only the context the
recipient lacks; most task briefs fit in about 220 words, and simple requests
can be much shorter. Go longer when required context, exact contracts, or
user-requested detail would otherwise be lost. This length limits the prompt,
not the recipient's answer.
Put output structure and any requested answer-length guidance together once.

Improve clarity without adding product scope, dependencies, metrics, or
approval gates the user did not ask for.

Routine gaps can remain for the recipient to resolve from its environment.
For a missing decision that changes the task, put the necessary investigation
or focused clarification into the prompt, before the affected action, instead
of inventing the decision or replacing the prompt with a question to the user.
When the request supplies no usable task at all, write a brief prompt asking
the recipient to establish the intended outcome before proceeding.

## Read only what changes composition

- Read [guidance.md](references/guidance.md) when uncertainty, multiple stages,
  evidence requirements, preservation, or an exact output contract makes the
  prompt difficult to compose. Apply the relevant distinctions together; do not
  force a request into one exclusive category.
- Read [coding.md](references/coding.md) for prompts about code, software
  behavior, development plans, implementation, or code review.
- Read [images.md](references/images.md) for image-generation or editing
  prompts, including GPT-image-2-specific guidance.

Examples illustrate judgment: apply the distinction that fits the request
without copying their headings, domain facts, or complete instructions. Keep a
simple request simple.

## Check the prompt, then return it

Write the prompt with [Writing style](../../references/writing-style.md).

Cut redundant sections before compressing sentences. Distinguish the
recipient's output format from this skill's output: if the user wants a prompt
requesting JSON, return that prompt, not JSON results.

Use no outer code fence unless the user requests one. Internal examples or
schemas may use fences. If the user asks for something other than a prompt, do
that instead.
