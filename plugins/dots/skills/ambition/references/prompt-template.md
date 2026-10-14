# Ambition prompt template

Use this skeleton when another model or a subagent should do the ambitious
pass. Replace each bracketed slot with task-specific content and delete slots
that do not apply. Keep the section order of the requested deliverable. A fixed order makes
answers from different models easy to compare and combine.

Contents: [Template](#template) · [Worked example](#worked-example)

## Template

```text
Context
[Product or project, who it serves, the current plan, and the materials to
read: files, mockups, data, prior decisions. The recipient cannot see our
conversation.]

Settled decisions and hard constraints
Do not reopen these unless you find strong evidence; you may push beyond them.
- [decision or constraint]
- [...]

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
7. Recommendation and staging.
8. Observations versus inferences, with uncertainty stated.
```

## Worked example

Illustrative, not a template to copy: a product-shaping session for an iPhone
app's AI assistant that logs food and workouts.

- **Altitude:** reframed "where does the assistant sit in the app?" into "what
  does the person want to have happen, and is 'logging' even the right verb?"
- **Depth:** four disciplines each answered the four questions: an Apple
  human-interface designer, a dietitian and nutrition researcher working from
  USDA AMPM recall methods and FNDDS food data, an iOS frameworks engineer,
  and an accessibility specialist.
- **Range:** Apple first-party patterns, dietary-recall science, calm
  technology, and game feel, plus a red team of a short-seller skeptic, a
  forensic auditor of the nutrition numbers, and a tired user mid-task.
- **Targets:** numeric targets that looked unreasonable, each paired with an
  outside judge.
- **Constraints:** the settled decisions were listed as "do not reopen unless
  strong evidence; you may push beyond."

The answer reframed the feature as "tell it only what changed, and never tell
it twice," caught an arithmetic error in the mockups through the forensic
audit, and killed two weak ideas before any were built.
