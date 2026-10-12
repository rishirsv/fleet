# Reviewing a skill

Diagnose the skill from source and existing evidence, one instruction at a
time, and produce findings with proposed edits. A review-only request leaves
source unchanged so the maintainer can take edits selectively. When the request
also authorizes fixes, apply the supported edits through the default
`skill-creator` workflow, including its criteria for behavioral trials.

Contents:

- [Scope and inventory](#scope-and-inventory)
- [Scan for defects](#scan-for-defects)
- [Findings](#findings)
- [Proposed edits](#proposed-edits)
- [Return the review](#return-the-review)

## Scope and inventory

Take the scope and decision from the request. A broad review covers every
instruction and resource the skill uses, related skill descriptions,
repository instructions, validation evidence, and existing evaluation
artifacts. A narrow review covers every file or behavior that can change the
requested diagnosis. State the scope and assumptions at the top of the review
instead of pausing to confirm them; the user can narrow the scope and rerun.

Identify the recurring job, related work it excludes, required inputs, common
and alternative workflows, output, evidence of completion, authorization
requirements, and stopping conditions. Inspect supporting domain references
only when their method can affect the diagnosis.

Before judging anything, inventory what the agent loads or runs: discovery
metadata (the frontmatter `description` and files such as `agents/openai.yaml`),
`SKILL.md` and each reference with the condition that loads it, scripts with
their arguments, output, and failure messages, assets, templates, embedded
examples, and descriptions the skill writes for tools, subagents, or other
skills. Include the inventory in the review so the user can correct it.

Then read each sentence, bullet, and example and ask what the agent would do
differently without it. Context only the author has (audience, deliverable,
environment facts, tool contracts, the quality bar, hard judgment calls, domain
methods, and reasons behind constraints) stays, and missing context is a
defect. A constraint on behavior needs a stated reason, a real ordering
dependency, or a reader or consumer that requires it. A restated default, such
as a generic virtue or behavior the agent shows unprompted, is a removal
candidate. A review that only tries to shorten the skill can delete context
the agent needs.

## Scan for defects

Check meaning before style. For a prose defect, identify the action or
condition that is unclear and report it in the writing style's prose-finding
form.

Check each instruction against the sections of
[standards.md](standards.md): discovery and description form, structure and
loading, instructions that change behavior, authority and stops, revisions to
an existing skill, and completion and evidence. Also look for:

- a single example the agent will copy as a template, or numeric limits no
  reader or consumer requires;
- a menu of equal alternatives where one default would do, and scoring
  language that describes a grader instead of stating the requirement;
- deterministic work left to the agent, such as lookup tables, arithmetic, or
  fixed formatting that a data file or script should own;
- validators that accept plausible bad results, and tests that assert wording
  rather than observable behavior;
- missing authorization, failure, stop, or partial-success behavior; and
- private, source-specific, or maintainer material in the runtime.

Search for textual signals: all-caps `MUST|NEVER|ALWAYS|CRITICAL|IMPORTANT`,
`try to|if possible|ideally`, runs of `Do not|Never|Avoid`,
`now|no longer|instead of` attached to rules, `STEP \d` sequences for judgment
work, and repeated sentences across files. A match is a lead; confirm it
against the classification above.

Leave these alone even when a search matches:

- context, as classified above;
- exact steps for fragile operations, such as destructive commands,
  authentication, compliance steps, or file formats where one sequence is safe;
- script and tool contract detail, such as arguments, limits, failure modes,
  and what a call does not return, which often needs more text;
- prohibitions against a failure that still occurs, or that encode a real
  business, data, or policy constraint;
- examples that pin a required output format;
- a one-line role statement, unless it replaces the audience and deliverable;
  and
- a single closing recap of the few key constraints.

Under-specification is a defect too: when a step is vague, a contract is
missing, or completion is undefined, the correction adds text. A file with no
supported defects is a valid result. Report a defect only when you can name
the pattern and its consequence for the job; otherwise record an open
question. Trace edge cases only when they can change the verdict.

## Findings

Separate direct observation from inferred consequence. Each finding includes:

- the location as `path:line` or a line range;
- the exact text, quoted;
- the pattern it matches, from this scan or the standards;
- the likely consequence and, if it is uncertain, what evidence would disprove it;
- a confidence level: high when source, a check, or a reproduced failure shows
  the defect; medium when it matches a named pattern with a concrete
  consequence; low when it rests on style or inference alone;
- an action: `remove`, `rewrite` with the replacement text, `move` with the
  destination, `add` with the new text, or `flag` with no edit; and
- static or behavioral evidence that could verify the correction.

Use the user's verdict and severity vocabulary when supplied. Otherwise lead
with `Accept`, `Accept with conditions`, `Revise`, or `Insufficient evidence`,
then order findings by likely consequence. Add a numeric score only when the
user supplies the question and scale.

Give every high- or medium-confidence finding a concrete action, even a minor
one, because the maintainer can decline it. Reserve `flag` for low-confidence
items and items outside the scope.

## Proposed edits

- Include high- and medium-confidence findings whose action is not `flag`,
  one finding per edit so the maintainer can take them selectively.
- Show each edit as a diff hunk against the current source, with the
  `path:line` and the finding it resolves. The removed lines match the source
  exactly, and the added lines are the full replacement text.
- Prefer a rewrite to a bare deletion when the instruction has a live purpose:
  restate the concern simply.
- Complete each removal by removing its dependents, as the standards describe.
  When stakes are high, trial contested removals one at a time so a regression
  points to its cause.
- Present the edits as the end of the review, without pausing midway or
  closing with a question about applying them. Apply edits when the request
  authorizes fixes, leaving `flag` and low-confidence items out of the
  applied set.

## Return the review

Return chat by default:

1. Verdict, scope, and assumptions.
2. The inventory.
3. Finding counts by pattern and the two or three highest-consequence findings
   in prose.
4. Findings in consequence order.
5. Proposed edits, including exact replacements for prose defects.
6. Relevant areas where no defect was supported.
7. Limits, `flag` items, and open questions that could change the verdict.

When the user requests a durable machine-readable review receipt, copy
[`review.json`](../assets/review.json) to the selected output location. Replace
every placeholder, repeat the finding and edit entries once per item, and
record the content hash of each inspected file that supports the verdict or a
finding. Leave the receipt unchanged after completing it, and recheck relevant
hashes before consuming it later.

When a claim needs fresh behavioral evidence, state the limitation and the
smallest useful forward test.
