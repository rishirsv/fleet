# Independent finish review

Use before delivering implemented UI from `$design`, including refinements and
reference recreations. Review only the changed workflow and plausible effects
of shared changes. A small edit gets a small review. Do not add a brief approval,
new product documents, a state file, a detector, or a new full-product audit.

## Builder handoff

After the normal rendered inspection, start one fresh, read-only subagent using
the host's available delegation tools. Give it the reviewer instructions below
by this file's absolute path; no named custom agent is required. Do not fork or
inherit conversation history (Codex collaboration: `fork_turns: "none"`). Supply
only:

- The original request, confirmed decisions, acceptance scope, and constraints.
- The accepted visual target when one exists; otherwise the chosen direction
  and relevant product/design-system sources. Label inspiration as inspiration.
- Changed implementation paths and the routes, viewports, themes, and states
  affected, with explicit required coverage and any known access gaps.
- Current captures and interaction evidence, with their paths and capture
  context, plus relevant existing test or detector findings when available.
- The absolute paths of this file, [craft floor](craft-floor.md), and
  [visual proof](evidence.md). For a visual target also pass
  [design QA](../skills/design/references/design-qa.md).

Send raw evidence rather than the builder's self-assessment or desired verdict.
Keep the packet in the tool call or existing task notes; no dedicated report
file is required. Reuse the existing captures after checking they show the
current implementation. Do not capture every viewport again just for handoff.

## Reviewer instructions

You are the independent finish reviewer. Read the provided references and
inspect the actual images before reading builder commentary or source code.
Read the accepted target first when present, inventory its salient elements,
then compare with the implementation. Edit nothing and start no server or build.
Use supplied evidence and read only relevant source; report access gaps instead
of inventing observations. Screenshots alone prove neither behavior nor motion.

Check these together in one scoped pass:

- **Evidence:** required captures exist, open, and show the correct route,
  viewport, theme, state, and current result. Reject blank, half-loaded,
  incomplete, or wrong-screen captures; an intentional loading state is valid
  when named. A valid capture showing UI clipping is defect evidence, not a
  reason to discard the capture.
- **Fidelity and commitment:** composition, reading order, first viewport,
  density, type character and hierarchy, imagery/material, background value
  and temperature, and primary action deliver the accepted target or chosen
  direction. Distinguish supported adaptation from missing or contradicted
  elements. An inspiration image is not an approved specification.
- **Craft and use:** enforce the craft floor, preserve accurate content and
  product conventions, and check the affected responsive, interaction, and
  accessibility requirements against the evidence. Visual ambition must suit
  the task. Keep strong qualities intact while fixing defects.

Return a short result:

1. `recapture`, `rebuild`, `fix`, or `ship`, scoped to what you reviewed.
2. Material findings, each with a stable ID, priority, location, expected versus
   observed result, evidence, and concrete correction. Use design QA's P0–P3
   severity when loaded; otherwise P0 blocks the task, P1 is a major failure,
   P2 is a material defect, and P3 is optional refinement. A violated aesthetic
   ban is at least P2 unless the packet supplies an explicit exception authority.
3. One line on what to preserve and any unverified required coverage.

Use `recapture` when required visual evidence is missing or invalid. Keep any
independently supported findings, but defer visual approval until valid evidence
is reviewed. Use `rebuild` when the central composition or material contradicts
the target and local patches cannot resolve it; name the regions and assets to
replace. Use `fix` for other P0–P2 findings or missing required nonvisual proof.
Use `ship` only with no open P0–P2 findings or required evidence gaps in scope.
Do not invent numerical quality scores or call uninspected scope approved.

## Corrections and verification

The builder acts within the original authorization. For `recapture`, obtain the
missing or corrected evidence and request a full scoped review on valid inputs.
For `rebuild`, rework the named regions and request a fresh full scoped review;
do not certify the replacement by scoring the rebuild instruction alone. If the
rework would discard approved content or exceed the request, report the decision
needed rather than silently expanding scope.

For `fix`, apply material corrections in one batch, inspect and exercise the
affected result, and return updated captures at matching states and viewports
to the same reviewer through agent continuation. Retain IDs and supply changed
paths plus evidence; the builder's claim that a fix landed is not verification.
The reviewer scores each ID `resolved`, `partial`, or `unresolved` from the new
evidence, checks regressions caused by that batch, and returns the disposition
again. Do not launch a new defect hunt or repeat unrelated checks. If continuing
the agent is unavailable, start a fresh reviewer with the original findings,
target, relevant references, and before/after evidence for the same scoring task.

Default to at most two correction batches in total, including recapture and
rebuild rounds, honoring a user's explicit budget.
Stop earlier when a batch resolves nothing, a concrete blocker prevents progress,
or scope requires a user decision. Report open IDs and evidence gaps; a budget
limit or builder override never converts a failed review to `ship`. A later
edit invalidates affected evidence and needs a scoped recheck. User evidence
contradicting a verdict triggers a new scoped review with that evidence included.

If delegation is unavailable or fails, use the same checks locally and disclose
that independent review did not complete. Do not describe a self-check as an
independent pass. Report the review's actual scope and open findings at delivery;
a follow-up scoring pass establishes the status of those fixes, not approval
of the whole product.
