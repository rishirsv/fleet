---
name: apply-ambition
description: "Develops more ambitious approaches to a task and the evidence needed to test them. Use when the user asks to push an idea further, raise its ambition, or prepare an ambitious brief for another model."
---

# Apply Ambition

Develop more ambitious ways to achieve the user's goal. Reconsider the desired
outcome, the depth of the work, and methods from other fields while preserving
settled decisions and constraints. Explore four dimensions:

- **Speed** reduces elapsed time through distinct parallel workstreams.
- **Altitude** moves from the task to the outcome behind it.
- **Depth** does the work the way the field's best practitioner would.
- **Range** brings in methods from other fields.

## Choose the mode

- **Apply directly** by default. Perform the ambitious pass on the user's
  actual task and deliver its results under Output. Do not stop at a prompt,
  worksheet to fill in, or description of how you would do the work.
- **Compose a prompt** when the user wants another model's or a subagent's
  view, or when an independent second opinion can find what the current
  conversation cannot. Use the [prompt template](#prompt-template) below
  and fill it from the conversation. The recipient cannot see this
  conversation, so include the product context, the current plan, and the
  materials it must read. When a subagent runs the prompt, combine its answer
  with your own work. Mark which of its claims you checked.

## Record what is settled first

Before any reframing, list the settled decisions and hard constraints. Mark
each one "do not reopen without strong evidence; you may push beyond it." The
work can then go past the plan without undoing choices the user already made.
Treat earlier assistant recommendations as inputs to test, not as settled
decisions.

## Speed: distinct subagent teamwork

Use parallelism when independent work is substantial enough to save time after
coordination and integration. Keep small or tightly coupled work with one owner.
Speed changes how the authorized work is delivered, not its scope.

1. **Find the dependencies.** Identify what blocks the outcome. Settle shared
   decisions before dispatching work that depends on them; keep independent
   investigation moving alongside the coordinator's work.
2. **Assign distinct contributions.** Give each subagent one bounded question
   or deliverable, the context and sources it needs, its dependencies, completion
   evidence, and a compact return format. Assign disjoint files or artifacts
   for edits. Shared interfaces and integration belong to the coordinator.
3. **Run the useful tracks together.** Use the smallest team that covers the
   independent work. For example, one agent investigates customer evidence,
   another tests technical feasibility, and a third develops the interaction
   approach against agreed constraints. Each produces a different input to
   the same decision. Do not send the whole task to every agent or create an
   agent merely to fill a discipline or persona.
4. **Integrate once.** Collect the outputs, reconcile consequential conflicts,
   and combine them into the requested result. Reuse valid checks and evidence;
   do not add a verifier for each worker. Run any required review within the
   selected review budget. Report unresolved dependencies rather than silently
   expanding assignments.

For a planning or prompt-writing request, describe the team and handoffs without
launching it. For authorized execution, use available subagents under the host's
permissions; if unavailable, perform the same distinct work sequentially.

## Altitude: move from the task to the outcome

- Ask what the person wants to happen after this task is done. Then ask what
  goal sits behind that goal. Restate the task at that level. For example,
  "fix this crash" becomes "keep the app free of crashes."
- Question the format itself. If the deliverable is a report, review, or
  screen, ask whether a different mechanism reaches the outcome sooner.
  Propose how to test that mechanism against past cases, and how to run it
  alongside the current one before replacing it.
- Change the workflow so the model can check its own progress. Name the data,
  tools, and access it needs to work without a person in the loop, for
  example crash reports, a map from release versions to commits, and a
  machine that can reproduce the bug.

A quarterly business review shows the climb in three steps:

1. Give the model all the raw data and ask what changed this quarter, why it
   changed, and what to do about it.
2. Ask for decisions instead of a summary: the three most urgent decisions,
   each with the arguments for and against.
3. Question the format: design a better way than a quarterly deck to catch
   problems early, test it against past quarters, and run it beside the
   current review for one quarter.

Altitude helps most when the work has a measurable outcome. Recurring
meetings and reviews often mark a task that would benefit from it. For
creative work or work that depends on taste, weight depth and range more
heavily.

## Depth: work like the field's best practitioner

Fill a depth worksheet for each relevant expert, named by discipline. For each
expert, answer four questions:

1. What would a top professional do here that the user did not request?
2. What is the rawest material they would start from?
3. Which specific methods, instruments, datasets, or tools would they use?
4. What, besides the user or the model, would verify the result?

Then rewrite the task to request exactly that work: a deeper version of the
task, not a bigger one. Apply these rules while you do it:

- Use the field's real instruments. Do not accept work that only borrows the
  field's vocabulary. Insist on the databases, statistical methods, and tools
  that practitioners use.
- Set specific, hard targets, with numbers where possible, and treat them as
  achievable. For example, ask for a 200 ms response instead of accepting 5 s.
- Test each assumption the plan depends on against raw data. Ask for the
  check directly: "Reproduce that result from the raw data."
- Aim to produce knowledge the user did not have, such as a simulation, a
  newly found blind spot, or a prediction tested on data the model has not
  seen.
- Give every target an outside judge: a test, dataset, benchmark, tool, or
  person independent of the model that produced the work. A tool the model
  can run for immediate feedback is the strongest judge. Self-grading does
  not count.

## Range: borrow from other fields

- Replace the deliverable's noun with the verb it serves. A quarterly review
  deck becomes "getting busy people to believe a cause-and-effect story and
  decide under uncertainty." Look for fields that do that verb well. This
  noun-to-verb move comes from Tom Kelley and Jonathan Littman's book "The
  Art of Innovation."
- Assemble a crew of disciplines beyond the obvious one. For the quarterly
  review, the crew might be an analyst, a journalist, an editor, and a motion
  or audio designer.
- Always include a red team: a skeptic who profits if the idea fails, such as
  a short seller; a forensic auditor of the numbers; and the real user at
  their least patient.
- Perform each discipline's work; do not role-play it. Write "audit these
  numbers the way a forensic accountant would: trace each figure to its
  source," not "you are a forensic accountant." A persona changes the voice
  of the answer without adding rigor. Use the Speed workflow when distinct
  contributions warrant parallel agents.

## Why hard targets work

Belief in what is possible often limits output. Psychology calls this belief
self-efficacy, and three findings support pushing it:

- **Specific, hard goals win.** In Edwin Locke and Gary Latham's review of
  goal-setting research, people with specific hard goals performed better
  than people told to do their best.
- **Belief that a problem is solvable changes the result.** In 1939, George
  Dantzig solved two open statistics problems because he took them for
  homework. After Roger Bannister ran the first four-minute mile in 1954,
  other runners soon did it too.
- **Permission to fail removes pressure.** "The Inner Game of Tennis" argues
  that trying too hard hurts performance. Linus Torvalds announced Linux as
  "just a hobby, won't be big and professional like gnu."

Model capability changes every few weeks. State targets that look
unreasonable, treat them as reasonable, and let the outside judges report
what the model reached.

## Output

Write prompts, critiques, recommendations, and the report with
[Writing style](../../references/writing-style.md). When delegating the writing,
supply this reference as a resolved file path the recipient can read, or include
its contents in the prompt.

Deliver these sections in this order. Include only the sections the task
supports:

1. The altitude reframe, in one or two sentences.
2. The depth worksheet and what it changed.
3. A blunt critique of the current plan.
4. Two or three more ambitious concepts. For each, give the steps, the moment
   that delights or convinces, what earns trust, the technical split, and the
   hardest risk.
5. Targets, each with its outside judge.
6. The top failure modes, each with a move that defuses it.
7. A recommendation with staging: what to do first, what to defer, what
   evidence would change the plan, and team assignments and handoffs when
   parallel work helps.
8. Observations separated from inferences, with the uncertainty stated.

If a section produces nothing new, say so in one line instead of filling it.
Report ideas the work killed and errors it caught; they are part of the
result.

## Prompt template

Use this skeleton when another model or a subagent should do the ambitious
pass. Replace each bracketed slot with task-specific content and delete slots
that do not apply. Keep the section order of the requested deliverable. A fixed order makes
answers from different models easy to compare and combine. Supply the
writing-style reference identified in `SKILL.md` as a resolved readable path
or its full contents, and instruct the recipient to read and apply it to
authored prose.

### Template

```text
Context
[Product or project, who it serves, the current plan, and the materials to
read: files, mockups, data, prior decisions. The recipient cannot see our
conversation.]

Settled decisions and hard constraints
Do not reopen these unless you find strong evidence; you may push beyond them.
- [decision or constraint]
- [...]

Speed
[Distinct workstreams, their owners, dependencies, completion evidence, and
who integrates them. Include only when parallel work helps. State whether the
recipient should propose the team or execute it within existing authorization.]

Altitude
Reframe the task from "[task as asked]" to the outcome: what does the person
want to have happen after this? [Name the verb or format that may itself be
wrong, e.g. "is 'X' even the right verb?"] Propose how a different format
would be tested against past cases and run alongside the current one.

Depth
For each expert below, answer: (1) what a top professional would do here that
was not requested, (2) the rawest material they would start from, (3) their
specific methods, instruments, or datasets, (4) what besides you or me would
verify the result. Then state what the worksheet changed in the plan.
- [discipline, with its real instruments or data sources]
- [...]

Range
Draw on [fields beyond the obvious one]. Run a red team: [a skeptic who
profits if this fails], [a forensic auditor of the numbers or claims], [the
real user at their least patient, mid-task]. Perform each discipline's work
directly; do not adopt personas.

Targets
Set specific, numeric targets that look unreasonable, and treat them as
achievable. Give each an outside judge: a test, dataset, benchmark, tool, or
person independent of the model. Self-assessment does not count.

Deliverable, in this order
1. Altitude reframe.
2. Depth worksheet and what it changed.
3. Blunt critique of the current plan.
4. Two or three more ambitious concepts, each with steps, the moment that
   delights or convinces, what earns trust, the technical split, and the
   hardest risk.
5. Targets with their outside judges.
6. Top five failure modes, each with a defusing move.
7. Recommendation and staging, including team assignments when useful.
8. Observations versus inferences, with uncertainty stated.
```

### Worked input prompt

This example shows a prompt supplied to an agent, not an answer or completed
work. Use it only to understand how to formulate a task-specific brief in
Compose a prompt mode. Its product, disciplines, and targets are illustrative;
when applying the skill directly, do the user's actual work instead.

```text
Help shape an iPhone app's AI assistant for recording food and workouts.
Use the supplied product context, mockups, and settled decisions.

Altitude
Question whether placing a logging assistant in the app is the right problem.
Identify what the person wants to accomplish and whether logging is the best
way to achieve it.

Depth
Apply the four depth questions to human-interface design, dietary-recall
research, iOS engineering, and accessibility. Consider USDA AMPM recall
methods and FNDDS food data where relevant. Identify unavailable evidence
rather than inventing results.

Range
Draw useful methods from Apple interface patterns, dietary-recall science,
calm technology, and game feel. Challenge the proposal from the perspectives
of someone skeptical of its value, an auditor of its nutrition calculations,
and a tired person using it mid-task. Perform the analysis rather than
role-playing those people.

Targets
Propose ambitious numeric targets and an independent way to test each.
Distinguish proposed targets from measured results.

Constraints
Preserve the supplied settled decisions. Explain any evidence that would
justify reconsidering one.

Deliver the ambitious analysis and recommendation for this product, following
the Output structure. Do not merely repeat these instructions or claim that
unperformed research, audits, or experiments have succeeded.
```
