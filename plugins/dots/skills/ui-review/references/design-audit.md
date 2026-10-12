# Design audit

Judge the quality of an interface or experience against its intended user and
task.

## Contents

- [Inputs](#inputs)
- [Choose the mode](#choose-the-mode)
- [Inspect and judge](#inspect-and-judge)
- [Design criteria](#design-criteria)
- [User experience criteria](#user-experience-criteria)
- [Classify findings](#classify-findings)
- [Result](#result)

## Inputs

- **Subject:** screen, component, flow, or product area and the user's question.
- **Context:** intended user, task, usage conditions, and governing design
  direction. Use established context and name assumptions that could change the
  assessment.
- **Evidence:** supplied screenshots or recordings, a live interface, and source
  or design-system material when relevant.

For a product-wide audit, inventory the relevant routes and recurring states
first. Inspect each primary view in scope with its representative populated,
loading, empty, and error states, and list the views and states you could not
reach.

## Choose the mode

| Request | Mode | Criteria |
|---|---|---|
| Appearance, visual hierarchy, identity, or craft | Design review | D1–D5 |
| Task completion, usability, flow, or accessibility | User experience review | U1–U7 |
| Both, or an unqualified review, audit, or readiness request | Combined review | D1–D5 and U1–U7, once each |

Choose the mode from the question; even one modal may need a UX review. If a
narrow mode exposes a material issue outside its scope, flag it and name the
additional review needed instead of claiming combined coverage.

## Inspect and judge

Use the criteria to check your first impression and assess every applicable
one. For user tasks, follow the important steps and recovery paths. Keep
observations tied to the captured state; intentional loading, empty, and error
states are valid evidence. Record blocked steps and unavailable checks as
coverage gaps, and mark each criterion as observed, unverified, or not
applicable.

Describe visible details precisely: counts, quoted copy, and relationships
between elements. Leave pixel values and behavior unguessed. Distinguish defects
from opportunities.

For repeated lists, inspect the densest representative viewport and exercise an
item's collapsed and expanded states. Count complete visible items and every
label, control, divider, or metadata line multiplied across them. Moving
low-value copy into a disclosure resolves nothing unless someone needs that copy
in the current view.

## Design criteria

| ID | Criterion | Inspect |
|---|---|---|
| D1 | Identity and visual language | Does the visual system suit the brief and carry a deliberate point of view? Assess palette intent, accent balance, and material character. Compare with category expectations only when useful; familiarity is not automatically the goal. |
| D2 | Hierarchy and composition | Does visual weight match importance? Identify the entry point, competing focal points, groupings, proportions, alignment, spacing rhythm, and optical balance. Judge the arrangement of visible content here; whether that content belongs is U2. |
| D3 | Typography | Family, role scale, weight, line height, tracking, measure, wrapping, and truncation. Judge visual reading quality here; contrast and user scaling belong to U6. |
| D4 | Assets and surface treatment | Imagery, crop, sharpness, masking, icons, stroke and optical consistency, borders, shadows, radii, and elevation. Do they reinforce the design or add noise? Accessible alternatives belong to U6. |
| D5 | Visual system consistency | Equivalent component appearances, token use, and visual variants across screens and states. Flag unexplained differences in repeated roles. Behavioral consistency and platform conventions belong to U3. |

## User experience criteria

| ID | Criterion | Inspect |
|---|---|---|
| U1 | Task entry and orientation | Can the intended user find where to begin, understand the available actions, know their current location or step, and predict what happens next? Check discoverability, wayfinding, scope, and expectations. Visual emphasis belongs to D2. |
| U2 | Information architecture and cognitive load | Does organization match the user's mental model and immediate task? Check grouping, prioritization, task-appropriate density, labels that restate visible context, duplicated dates, totals, or metadata, repeated disclaimers, instructions that paraphrase adjacent controls, and source or internal metadata more prominent than its usefulness. Judge recurring content across a representative viewport. A disclosure still costs an interaction; keep hidden content only when it supports the current task. Keep risk, coverage, approval status, and essential functions available at the point of decision. |
| U3 | Actions, flow, and conventions | Can the user complete the task with sensible steps and effort? Check controls, navigation, defaults, selections, reversibility, transitions between steps, interaction consistency, and platform conventions. For repeated items with optional detail, test collapsed and expanded states; prefer one accessible disclosure control within the item over a separate closed-state detail row. Test gesture discovery and visible alternatives. |
| U4 | States, feedback, and recovery | Loading, empty, success, error, validation, disabled, and other reachable states. Is feedback timely, entered data preserved, failure recoverable, and the next step clear? Warnings should appear with their condition, explain the consequence, and offer an action when one exists; persistent warnings without a current consequence add noise. Check whether controls and feedback already communicate routine workflow state before asking for explanatory prose. Assess motion as state and continuity feedback; motion accessibility belongs to U6. |
| U5 | Content and trust | Are labels, instructions, calls to action, claims, and terminology accurate and clear? Examine informed choices, consequences, reassurance, and misleading promises. Judge meaning and tone here; type styling belongs to D3. |
| U6 | Inclusive operation | Text and control contrast, non-color cues, semantics, reading order, keyboard reachability, focus, labels, accessible names and alternatives, target sizes, zoom and reflow, text expansion, assistive-technology behavior, and reduced-motion and timing needs. Name the evidence each claim requires. |
| U7 | Emotional and situational fit | Does the experience respect the user's likely stress, attention, expertise, frequency of use, and environment? Identify reward, encouragement, and helpful details suited to the user's circumstances. Distinguish contextual hypotheses from observed user research; praise or celebration is not universally appropriate. |

## Classify findings

Classify each finding by the cause that needs correction and include all its
effects in that one finding. A weak contrast ratio belongs to U6 even when it
also weakens hierarchy. Excessive content belongs to U2; poor spacing of
necessary content belongs to D2. Group symptoms with the same cause into one
finding.

## Result

Report as the skill's report section describes. For readiness, name what blocks
acceptance. Keep routine criterion accounting out of the report unless
requested.
