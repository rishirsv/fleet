# Component stress

Stress test or harden a component, or build a reproducer for a concrete content
or layout failure.

## Contents

- [Select reachable scenarios](#select-reachable-scenarios)
- [Scenario axes](#scenario-axes)
- [Render the real component](#render-the-real-component)
- [Inspect and report](#inspect-and-report)

## Select reachable scenarios

Identify the requested components. Read each component's props, slots, and data
constraints, where it manages state, and which screens use it. Test only
properties that vary, and include a scenario only when the component can receive
that input or reach that state in production.

Pick the applicable axes below and add project-specific extremes, bounded by
real data and supported layouts. Keep a short scenario plan beside the test page
or native preview fixtures and record exclusions that affect coverage. Test the
selected cases without combining every property.

## Scenario axes

**Content length**, when the component renders variable text such as user
input, CMS content, API data, or translations:

| Scenario | What it catches |
| --- | --- |
| Empty string | Collapsed boxes, floating labels with nothing to float over, placeholder-only inputs |
| One word | Buttons and badges sized to their longest expected content |
| Typical content | The baseline the others are judged against |
| Several sentences | Wrapping, multiline line height, containers that assumed one line |
| One unbreakable string | A long URL or `Donaudampfschiffahrtsgesellschaft`: overflow with no wrap opportunity |

**Content shape**, when text can come from users or locales the team does not
write in:

| Scenario | What it catches |
| --- | --- |
| Emoji, alone and mixed into text | Line-height jumps, broken vertical centering, truncation splitting a character |
| RTL text | Direction handling, punctuation on the wrong side |
| Mixed-direction text | An LTR product name inside an RTL sentence, and the reverse |
| Diacritics and tall scripts | Clipped ascenders and descenders in tight line boxes |
| Numbers where columns align | Changing digit widths moving values in tables and timers |

**Quantity**, when the component repeats over items such as lists, tables,
grids, tag rows, or avatar stacks:

| Scenario | What it catches |
| --- | --- |
| Zero items | Blank regions, missing empty states |
| One item | Layouts designed around plural content |
| The realistic count | The baseline |
| Ten times the realistic count | Missing scroll or pagination, performance collapse, sticky elements unsticking |

**Container**, when the component's available space varies. Use its smallest and
largest supported containers, and test viewport changes too when viewport rules
govern its layout:

| Scenario | What it catches |
| --- | --- |
| Smallest supported container (for example, 320px) | Clipping, horizontal scroll, controls escaping the box |
| Squeezed by a flex or grid sibling | Overflow from min-content sizing, a component refusing to shrink |
| A very wide container | Unbounded measure, stretched controls, content pinned to opposite edges |

**State**, only for states the component can reach through props, interactions,
or supported test adapters:

| Scenario | What it catches |
| --- | --- |
| Loading | Layout shift when content arrives, spinners with no accessible name |
| Error | Messages that overflow, color as the only signal |
| Disabled | State recognition, explanation, and focus behavior; apply the relevant contrast exceptions |

Exercise real focus and hover, state transitions, cancellation, and repeated
input where supported; static state fixtures cannot prove transition behavior.

**Environment**, only for modes the project supports. Use the app's real theme
controls and browser or platform settings for dark mode, zoom, text scaling,
reduced motion, and forced colors. Redeclaring tokens around a fixture tests a
different theme. Record which modes you exercised and which were unavailable.

## Render the real component

For web components, import the real component into one temporary page. Render
one instance per scenario in a single column with a short text label above each.
For native components, use named native preview fixtures with the same plan.

Use the app's fonts, tokens, providers, and supported theme controls. Keep
fixtures local and deterministic, out of production imports, and away from live
data. Preserve the project's server and client separation, using its existing
preview, story, or test adapter where available instead of making the whole
test page client code. Check that each instance received its intended fixture
before calling its output a failure.

Use bounded containers for component-width cases. Resize the viewport separately
when media queries, page chrome, or viewport units affect the result. Drive
internal states through their real interactions or supported test adapters.

## Inspect and report

Render every selected scenario and exercise the relevant input, focus, and state
transitions. Report a failure only after observing it, marked beside its
scenario, and record unavailable checks separately.

Report the failing scenario and what visibly or behaviorally broke. "Text
escapes the field's right edge" gives a correction a target; "spacing feels
tight" does not. If all checks pass, report only the tested scope.

A test-only request reports findings. When fixes are also requested, correct the
component, then rerun the failing cases and the other cases the correction could
affect. Keep the test page or native preview fixtures available, state how to
open them, and list checks that remain unverified.
