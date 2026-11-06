# Component stress

Stress test or harden a component, or build a reproducer for a concrete content
or layout failure.

## Contents

- [Select reachable scenarios](#select-reachable-scenarios)
- [Map the surface](#map-the-surface)
- [Worst-case values](#worst-case-values)
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

## Map the surface

Read the component and list every value it renders, with its source:

| Field | Source | Type | Limit | Optional? |
| --- | --- | --- | --- | --- |
| `name` | `member.name` | string | 255 (`schema.ts:14`) | No |
| `email` | `member.email` | string | none found | No |
| `role` | `member.title` | string | 120 | Yes |
| `status` | enum | `active` / `invited` / `expired` | — | No |
| `count` | `workspace.memberCount` | int | — | No |

Include the values people forget: counts in headers, relative timestamps, badge and status text, button labels that come from data, tooltips, avatar images, the list itself (its length is a value too).

Look up limits in the validation schema (Zod, Yup, Valibot), database migrations, API types, and form `maxLength` attributes. Note where the frontend and backend disagree; a 50-character input that saves to a 255-character column means something longer will turn up eventually, through an import or the API.

**Completion criterion:** every rendered value is in the table, with a source and either a limit or "unbounded".

## Worst-case values

Two failure modes, and the first is worse:

1. **Nonsense data.** `"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"` and 5,000-character names prove nothing. The designer will rightly say "that never happens" and stop listening. Every worst-case value must be something a real user could plausibly produce, or the longest value the backend actually accepts.
2. **Stopping at long text.** Long names are the obvious break. The ones that ship are the short name that leaves an orphaned dash, the missing avatar, the count of exactly 1 ("1 members"), the empty list, the badge whose text got translated.

Each worst-case value is either a realistic example (a real naming pattern, a real email shape) or the actual limit from the validation schema, database column, or API contract. If you find no limit, that's a finding in itself: say "unbounded" and test something long but believable. Pick values from the [worst-case catalog](stress-catalog.md).

A single worst-case dataset should hit every row of the catalog that applies to this component at once. Mix them across rows (row 1 is the long name, row 2 is the long email, row 3 is the one-letter name), as real data does.

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

Each of these signatures appears in the screenshot. The cause in the middle
column is almost always it. Truncation and tabular numerals are in
[Typography](../../design/references/typography.md).

| What you see | Cause | Fix |
| --- | --- | --- |
| Avatar or icon squished into an oval or pill | Flex child shrinking | `flex-shrink: 0` on the avatar, icon, and any fixed-size box |
| Text overflows its box instead of wrapping or truncating | Flex/grid child has `min-width: auto` | `min-width: 0` on the text column (`minmax(0, 1fr)` in grid) |
| Email or URL runs past the edge | No break opportunities in the string | `overflow-wrap: anywhere` on that element |
| Trailing action (••• menu, button) pushed off-screen or clipped | Middle content took all the space | `min-width: 0` on the middle, `flex-shrink: 0` on the action |
| Badge wraps onto two lines | Badge allowed to shrink | `white-space: nowrap; flex-shrink: 0` on the badge, and decide what yields instead |
| Avatar centered against a three-line name looks adrift | `align-items: center` on rows of varying height | Top-align (`align-items: flex-start`) once text can wrap, |
| Last row cut off at a hard edge mid-glyph | Fixed-height container with no fade or scroll affordance | Visible scrollbar or a fade mask, and ensure `overflow` is intended |
| Long word breaks mid-word in a heading | `word-break: break-all` | `overflow-wrap: anywhere` breaks only when it has to |
| Wrong initials (`"J"` for "Jo", `"CI"` for "… Montgomery III", `"�"` for an emoji-first name) | `.split(' ')[0][0]` style code | Initials from grapheme clusters (`Intl.Segmenter`), first + last word, fallback icon |
| Orphaned `—` or empty line where the role was | Placeholder rendered for a missing optional field | Omit the line, or reserve its height intentionally |
| "1 members", "0 member" | Hardcoded plural | `Intl.PluralRules`, or separate strings per count |
| `1284`, `1,284.000000001`, `NaN`, `undefined` | Raw number rendered | `Intl.NumberFormat` with the user's locale; guard null |
| Long translated button label overflows | Fixed-width button | Width from content with `min-width`, never a fixed `width` |
| Diacritics or tall scripts (Vietnamese, Thai) clipped top or bottom | Tight `line-height` with `overflow: hidden` | Looser `line-height` or no clipping on text boxes |
| Broken-image icon in the avatar | No `onError` fallback | Fall back to initials; `object-fit: cover` for any aspect ratio |
| Scrolling 1,000 rows stutters | Every row rendered | Virtualize, or paginate, and say which |
| Content renders raw `<b>`, `&amp;`, or `**text**` | Wrong escaping layer | Escape once, at render; never `dangerouslySetInnerHTML` user data |

Report one row per break, worst first. Severity: **Broken** (content unreadable, action unreachable, wrong data shown), **Ugly** (readable but visibly wrong: squished avatar, wrapped badge), **Fragile** (fine now, one realistic step from breaking: no limit, no fallback). Then list the breaks with more than one right answer (truncate vs wrap for a field, what an empty role should show, whether a 1,000-row list paginates or virtualizes), one line each with a recommendation, and the worst cases the component already handles.

A test-only request reports findings. When fixes are also requested, correct the
component, then rerun the failing cases and the other cases the correction could
affect. Keep the test page or native preview fixtures available, state how to
open them, and list checks that remain unverified.

Scenario axes adapted from Jakub Krehel's public break (jakubkrehel/skills, commit 60bf140); field map,
worst-case values and failure signatures from Emil Kowalski's public
break-ui (emilkowalski/skills, commit c8a7962). See the [Krehel](../../../references/jakub-krehel-LICENSE.txt)
and [Kowalski](../../../references/emil-kowalski-LICENSE.txt) licenses.
