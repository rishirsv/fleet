---
name: ambition
description: "Raises a task's ambition through altitude, depth, and range, either directly or as a prompt for another model. Use when the user asks to be ambitious, push work further, or get a second model's ambitious take."
---

# Ambition

Make the current task more ambitious without making it merely bigger. Apply
the framework from Felix Rieseberg's
[How to Be More Ambitious: A Tutorial for Humans with Models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/).
Skip speed (the same work, faster); it needs no method.

## Choose the mode

- **Apply directly** by default: run the moves below on the current task and
  deliver the result in the output shape at the end.
- **Compose a prompt** when the user wants another model's or a subagent's
  view, or when an independent second opinion would catch what the current
  context cannot. Read [prompt-template.md](references/prompt-template.md) and
  fill it from the conversation. The recipient cannot see this conversation,
  so include the product context, current plan, and materials it must read.
  When a subagent runs it, integrate its answer and mark which claims you
  verified.

## Record what is settled first

List the settled decisions and hard constraints before any reframing, each
marked "do not reopen without strong evidence; you may push beyond it." This
lets the work push past the plan without undoing choices the user already
made. Treat earlier assistant recommendations as inputs to test, not settled
decisions.

## Altitude: from the task to the outcome

- Ask what the person wants to happen after this task is done, and the goal
  behind that goal. Restate the task at that level.
- Question the format itself. If the deliverable is a report, review, or
  screen, ask whether a different mechanism reaches the outcome sooner, then
  propose how to test it against past cases and run it alongside the current
  one.
- Change the workflow so the model can check its own progress: name the data,
  tools, and access that would let it work without a human in the loop.

Altitude fits outcome-driven work best. For creative or open-ended taste work,
weight depth and range more heavily.

## Depth: work like the field's best practitioner

Fill a depth worksheet for each relevant expert, named by discipline. For each,
answer:

1. What would a top professional do here that was not requested?
2. What is the rawest material they would start from?
3. Which specific methods, instruments, datasets, or tools would they use?
4. What, besides the user or the model, would verify the result?

Then rewrite the task to request exactly that: a deeper version of the task,
not a bigger one. Also:

- Set specific, hard targets, numeric where possible, and treat them as
  achievable. Specific hard goals outperform "do your best."
- Test each load-bearing assumption against raw data rather than restating it.
- Aim to produce knowledge the user did not already have, such as a new signal,
  a simulation, or a measured comparison.
- Give every target an outside judge: a test, dataset, benchmark, tool, or
  person independent of the model that produced the work. Self-grading does
  not count.

## Range: borrow from other fields

- Replace the deliverable's noun with the verb it serves. "A review deck"
  becomes "getting busy people to believe a cause-and-effect story and decide."
  Search fields that do that verb well.
- Assemble a crew of disciplines beyond the obvious one, and always include a
  red team: a skeptic who profits if the idea fails, a forensic auditor of the
  numbers, and the real user at their least patient.
- Perform each discipline's work; do not role-play it. Write "audit these
  numbers the way a forensic accountant would: trace each figure to its
  source," not "you are a forensic accountant." Personas add voice, not rigor.

## Output

Deliver, in this order, only the sections the task supports:

1. The altitude reframe, in one or two sentences.
2. The depth worksheet and what it changed.
3. A blunt critique of the current plan.
4. Two or three more ambitious concepts, each with steps, the moment that
   delights or convinces, what earns trust, the technical split, and the
   hardest risk.
5. Targets, each with its outside judge.
6. The top failure modes, each with a move that defuses it.
7. A recommendation with staging: what to do first, what to defer, and what
   evidence would change the plan.
8. Observations separated from inferences, with uncertainty stated.

When a section produces nothing new, say so in one line instead of padding
it. Expect and report killed ideas and caught errors; they are part of the
value.
