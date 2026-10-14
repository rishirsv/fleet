---
name: ambition
description: "Raises a task's ambition through altitude, depth, and range, either directly or as a prompt for another model. Use when the user asks to be ambitious, push work further, or get a second model's ambitious take."
---

# Ambition

Make the current task more ambitious without only making it bigger. People
and models both aim too low: model capability is strong in some directions and
weak in others, so the request sets the ceiling. This skill raises that
ceiling in three ways:

- **Altitude** moves from the task to the outcome behind it.
- **Depth** does the work the way the field's best practitioner would.
- **Range** brings in methods from other fields.

A fourth kind of ambition, speed, does the same work faster. It needs no
method, so this skill skips it.

The framework comes from Felix Rieseberg's essay "How to Be More Ambitious: A
Tutorial for Humans with Models." This skill contains everything it needs from
that essay.

## Check the prerequisites

Ambitious work needs a model that can act. It needs a computer to run work on,
permission to install the tools a practitioner would use, and access to the
real data through files, connectors, or exports. Name any missing item before
you start. If an item stays missing, say how it limits the result.

## Choose the mode

- **Apply directly** by default. Run the moves below on the current task and
  deliver the result in the order given under Output.
- **Compose a prompt** when the user wants another model's or a subagent's
  view, or when an independent second opinion can find what the current
  conversation cannot. Read [prompt-template.md](references/prompt-template.md)
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
  of the answer without adding rigor. With several models or subagents, give
  each discipline its own agent.

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
7. A recommendation with staging: what to do first, what to defer, and what
   evidence would change the plan.
8. Observations separated from inferences, with the uncertainty stated.

If a section produces nothing new, say so in one line instead of filling it.
Report ideas the work killed and errors it caught; they are part of the
result.
