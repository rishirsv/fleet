# Motion review

Use for product interaction motion. Showcase choreography belongs to
`$design-to-motion`; use the shared motion guidance when evaluating its website
behavior. Choose the mode before inspecting:

| Request | Work | Result |
|---|---|---|
| Review a transition or change | Inspect the scoped motion and its states | Findings and verdict |
| Improve motion across a product | Inventory and sample relevant motion, then prioritize | Audit and actionable plans |
| Find opportunities | Look for candidate changes and test each against the gate | Opportunities and rejected candidates |

A review or opportunity search is read-only unless the user also requests
changes. Do not claim product-wide coverage from a sampled route.

## Gate and inspect

For each candidate, ask in order: **Should this animate at all? What is the
purpose?** Consider frequency, task, attention, and platform conventions. If
motion would slow or obscure the task, propose an immediate state change or
static feedback. For retained motion inspect entry, exit, origin, timing,
continuity, interruption, repeated activation, gestures, and reduced motion as
applicable. Reuse established tokens and components; avoid contradictory motion
systems.

Observe a running interaction when possible. Record or slow it and scrub through
intermediate frames to identify where a problem occurs; relate each finding to
the element, trigger, phase and relevant value. Exercise rapid reversal and
repetition at normal speed too: a slowed recording cannot establish
responsiveness. A screenshot shows an endpoint, not continuity. Source code
can establish implementation defects but cannot prove how movement feels.
Record device, viewport, input method, motion preference and coverage gaps.
Use platform-appropriate profiling when frames drop; distinguish measured
bottlenecks from guesses and do not transfer web compositor rules to native UI.

## Report

- **Focused review:** location, evidence, user impact, specific correction and
  verification for each finding, then a scoped verdict and coverage gaps.
- **Product audit:** inventory the inspected surfaces, group causes, prioritize
  by user impact, and provide implementation-ready plans with paths or
  components, intended behavior, and verification. Do not change source unless
  requested.
- **Opportunities:** list the proposed trigger, purpose, motion treatment and
  expected benefit. Also list plausible candidates rejected by the gate and
  why they should stay still. Do not invent durations where feel or platform
  behavior requires testing.

Based on Emil Kowalski's public [review-animations, improve-animations, and
find-animation-opportunities](https://github.com/emilkowalski/skills/tree/2d228630ba1446365f614a108cb8252f1feda202/skills),
adapted for web and native product interfaces.
