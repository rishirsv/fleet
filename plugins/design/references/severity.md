# Severity and verdict

One scale for every review mode, design QA and finish review. Each mode keeps
its own findings format and action verdict; severity and the threshold for
Block come from here.

## Evidence, not taste

Press hard on the escalation triggers and leave deliberate project choices alone. A trigger is a failure whatever the style guide says. A density, radius or voice you merely disagree with is not a finding.

The bar for reporting is evidence. The bar for `Approve` is that you inspected what you claim to have inspected.

## Rank by user impact

- `HIGH`: blocks a task, misleads the user, hides content or controls, causes data-loss risk or creates a repeated systemic failure.
- `MEDIUM`: meaningfully harms comprehension, efficiency, adaptability or consistency.
- `LOW`: isolated polish with limited task impact.

Within a severity, rank by how many places the finding reaches and how much one fix buys. A token or shared-component fix outranks the same symptom in one leaf.

**Escalation triggers.** Once confirmed, each of these is `HIGH` on sight, never averaged down because the surface is minor:

- A destructive action with no confirmation, undo or distinct treatment.
- Truncated content with no way to reach the full value.
- Content or a control reachable only past a scroll edge or behind a disclosure that has no visible cue.
- An error that names no way to recover from it.
- A semantic color used against its meaning, such as the danger hue on a non-destructive action.
- A state change carried by motion alone, with no color, icon or label left behind when the animation does not run.

Triggers rank above every other finding. When more fire than the cap allows, list them first and say how many the cap excluded. A cap may shorten a report; it may never be why a blocker went unreported. These set severity, not new rules.

## Prefer the cheaper fix

Severity says how bad a finding is; this says which fix to propose. When more than one would work, take the earliest that does:

1. **Delete.** A separator that space would carry, an animation on a high-frequency interaction, an attribute or wrapper the native element makes redundant, a ramp nothing imports.
2. **Use the platform.** The native element, the native control or the system's own focus ring, in place of a custom rebuild.
3. **Reuse what the project has.** An existing token, spacing step or motion curve, before any new value.
4. **Correct the value.** The wrong easing, radius, gap or color, using the exact value the owning reference gives.
5. **Add.** A new token, a wrapper, a layout rule, an attribute the platform cannot supply.

When the work under review adds what **Delete** would fix, that is a finding, and its correction is the deletion.

## Consolidate systemic findings

One root cause is one finding, with every confirmed location in the same row. Report at most 15 findings. Never pad toward the cap; a short review or no findings is a valid result.

Number findings in rank order so the user can answer "fix 1, 2 and 5". When fixes follow a review, fix only the numbers chosen.

## Verdict

End a review with one of two:

- `Block`: one or more `HIGH` findings remain. Do not ship until they are fixed.
- `Approve`: no `HIGH` findings remain. Any `MEDIUM` and `LOW` findings stay listed as work to do.

`Approve` covers only what was inspected. Name every area not reviewed in the verdict line.
