# Design QA

Check whether an implementation matches its accepted design and remains usable,
and correct it when the request includes fixes. To judge whether the accepted
design itself should change, use `$design-review`.

## Contents

- [Inputs](#inputs)
- [Map the design onto the project](#map-the-design-onto-the-project)
- [Compare](#compare)
- [Rubric](#rubric)
- [Classify findings](#classify-findings)
- [Severity](#severity)
- [Iteration loop](#iteration-loop)
- [Result](#result)

## Inputs

- **Expected result:** accepted visual target, relevant behavior requirements,
  and agreed deviations. A written brief alone is not a visual fidelity target.
- **Actual result:** rendered implementation, with live access when behavior
  must be exercised; source may help locate fixes.
- **Comparison scope:** matching route, viewport, scale, theme, content, auth,
  and interaction state; supported adaptations and states to check.

If the target or implementation cannot be inspected, report fidelity as blocked.
Continue checks supported by available evidence without inventing the missing
target. For a comparison request, report findings without changing the
implementation. For a build or correction request, make corrections within the
requested scope.

## Map the design onto the project

Before building from a design file, map every design value to what exists:

| In the design | In code |
| --- | --- |
| A bound variable or style | The token with the same name or the same value |
| A raw value that equals a token | That token |
| A raw value with no token | The nearest existing token, listed in the report as rounded |
| A component instance | The project's component of that name, with the variant the design shows |
| A component instance with no project equivalent | Plain markup in place, listed as a deviation, and ask whether a component should exist |
| A one-off group of layers | Plain markup in place, not a new component |

Never add a token, a component variant or an arbitrary value to hit a number. Ask which way to go when rounding would visibly change the design: more than `2pt` on spacing or size, or a color landing on a different step. Build the frames, breakpoints and states the file draws; a state it does not draw is not yours to design, so leave the component's default and list it as missing. A diff wider than the design is the most common way this goes wrong.

## Compare

Compare the target and implementation at matching dimensions and states. Use
matching crops and account for device frames and browser controls. Put both in
one comparison view rather than judging them one after the other, and add
detail crops where small differences matter. Match pixel density first: scale a
2x capture to a 1x target, or capture at the target's density, and record both
sizes and the scale used. A difference caused only by density, browser chrome,
or a device frame is not a finding.

Cover every applicable rubric category and exercise required controls and
states. Captures establish appearance; navigation, recovery, keyboard behavior,
and motion need interaction evidence. For behavior omitted from a mock, use the
task and platform requirements. Mark unspecified expectations and unavailable
evidence explicitly.

## Rubric

| ID | Criterion | Compare |
|---|---|---|
| Q1 | Structure and geometry | Content order, grouping, frame and crop, grid tracks, proportions, density, alignment, margins, padding, gaps, component sizes, and above-the-fold composition at the reference viewport. |
| Q2 | Typography | Family and fallback, weight, size, line height, tracking, optical balance, wrapping, truncation, and text density. Separate rendering-environment differences from correctable ones; do not infer an exact font from an indistinct capture. |
| Q3 | Color and surfaces | Palette and token mapping, foreground and background balance, gradients, opacity, state colors, borders, radii, shadows, and elevation. Contrast usability belongs to Q8. |
| Q4 | Images and icons | Account for every target asset: subject, crop, scale, aspect ratio, sharpness, compression, transparency edges, masks, style, stroke, and optical size. Flag missing assets and approximations. |
| Q5 | Copy and content | Preserve approved copy, labels, and content structure. Distinguish dynamic data from fixed copy; check standalone meaning, realism, and instructions or invented claims shown in product copy. Flag the brief leaking into the product: prompt wording, design notes, or demo and prototype controls shown as product UI. Text geometry belongs to Q2. |
| Q6 | Required behavior | Navigation, links, buttons, tabs, menus, selections, forms, filters, tooltips, media, and other required actions produce the intended result. Check hover, active, selected, and disabled states, transitions, validation, loading, empty, error, and success behavior, recovery, data preservation, feedback timing, and motion interruption. Add states only where the control needs them. |
| Q7 | Adaptive layout | At supported sizes, orientations, and content extremes, essential information and controls stay usable with no collisions, unintended overflow, clipping, collapsed regions, or destructive reordering. Use supplied targets where they exist and established adaptation requirements elsewhere. Zoom and text scaling belong to Q8. |
| Q8 | Accessibility conformance | Contrast, semantics, labels, alt text, reading order, keyboard and focus behavior, target sizes, non-color status cues, reduced motion, timing, text scaling, zoom, and assistive-technology requirements. Name untested requirements; visual similarity cannot establish conformance. |

## Classify findings

Assign each defect one primary category by its cause: a wrong font that changes
wrapping is Q2; a correct font clipped only at narrow widths is Q7; clipping
under user text scaling is Q8. Link effects across categories without counting
the same defect twice.

- **Implementation defect:** violates the accepted target or an applicable
  behavior, adaptation, or accessibility requirement. Correct within scope.
- **Agreed adaptation:** an intentional, supported difference. Record it and
  exclude it from the defect count.
- **Source-design issue:** a problem reproduced from the accepted design. Assess
  it with `$design-review` and keep the target unchanged until a design decision
  resolves it. If it also violates an explicit acceptance requirement, keep
  that requirement blocked.
- **Unspecified or unverified:** evidence or a governing decision is missing.
  Name the gap.

## Severity

Use the plugin's [severity](../../../references/severity.md) scale. For fidelity:

| Level | Consequence |
|---|---|
| HIGH | Core task impossible, unusable layout, major mismatch, or usability regression |
| MEDIUM | Material visual difference, inconsistent behavior, or a layout or refinement defect |
| LOW | Minor refinement that does not block the declared acceptance scope |

Classify persistent controls hidden by overflow as MEDIUM or higher. Use the same
severity for differences that materially change major proportions, wrapping,
density, or first-viewport content.

Each finding names location, expected and actual result, evidence, impact, and a
concrete fix. Name the responsible component or token when known. Report
differences that matter to the acceptance scope; leave optional aesthetic
changes out of fidelity findings.

## Iteration loop

For build or correction requests, iterate toward the declared acceptance scope,
respecting any user-specified limit. A comparison-only request reports findings
without entering the loop. One iteration is **compare → fix → capture → compare
again**:

1. Compare the current implementation with the target and prioritize HIGH and
   MEDIUM findings.
2. Apply the material corrections within scope.
3. Capture the revised implementation at matching viewports and states, and
   exercise affected behavior.
4. Compare again, linking each original finding to its fix and post-fix
   evidence. Carry unresolved findings and regressions into the next iteration.

For implementation or correction work, use [finish review](../../../references/finish-review.md)
as the final comparison and independent verification of material corrections.
Pass this rubric and accepted target to the fresh reviewer. Its correction
batches are part of this loop, not a second iteration budget. A comparison-only
request needs no additional reviewer and authorizes no fixes.

Build, lint, deployment, and preview troubleshooting do not count as design
iterations. Recheck other areas a change could affect. Stop when the requested
limit (or finish review's default budget) is reached, no actionable HIGH or
MEDIUM findings remain, or a concrete blocker prevents progress. If the same defect
survives two attempted fixes without new
evidence, investigate its cause or report why progress is blocked. Do not
repeat a whole audit for a local repair unless its effects warrant it. A clean
initial comparison needs no correction cycle.

## Result

Report each compared element as matching, rounded to a token, or deviating, then
list, one line each, what is unwired (rendering from fixtures until the data
exists), the states the design does not draw, and where the design breaks a
rule, with the reference that owns it:

| Element | Design | Built | Status |
| --- | --- | --- | --- |
| Card padding | 20 | `spacing-5` | Matches |
| Title size | 15 | 14, `body-sm` | Rounded to token |

Record source and implementation evidence, comparison scope, findings, agreed
adaptations, unverified checks, and iterations completed (with any user-specified
limit). For each correction, keep the original finding, change made, and post-fix result in
the task's existing notes or artifact.

Use **passed** when no actionable HIGH or MEDIUM defect or required evidence gap
remains in the declared scope; LOW follow-ups may remain. Otherwise use **blocked** and
name what remains, including fixes not authorized in a comparison-only request.
Reaching the iteration limit does not make unresolved QA pass. A fidelity pass
does not certify the quality of the source design or untested accessibility and
behavior.

Design-to-project mapping adapted from Jakub Krehel's public build-design (jakubkrehel/skills, commit 60bf140). See [license](../../../references/jakub-krehel-LICENSE.txt).
