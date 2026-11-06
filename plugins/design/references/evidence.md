# Evidence for product design

Inspect the rendered surface before making visual claims. Exercise interactions
before claiming they work. Source code establishes implementation facts, not
appearance. Supplied screenshots can ground a design but cannot prove current
behavior, keyboard access or screen-reader output.

Use the user's selected surface and the active host's browser/native-tool
instructions. Otherwise prefer an available in-app browser for web and an
available native simulator or preview for native UI. Discover capabilities;
do not assume a named MCP server exists. If access fails, report the missing
coverage and continue only work that does not depend on it.

Keep a compact capture record in the task's existing notes or scratch artifact:
route/screen, viewport, scale when known, theme, content/auth state, interaction,
capture location and observation. Reject blank, loading, wrong-tab or login
captures as evidence of the intended screen. Do not expose sensitive content.

For fidelity comparisons, inspect source and implementation together in one
comparison view at matching state, crop and viewport. Include focused regions
when full-view details are unreadable. Distinguish source defects from drift.
Do not substitute a remembered image or an inferred font measurement for evidence.

Cover the changed workflow, narrow/wide layouts and material reachable states.
For a flow audit, number the steps and record the task, action, observed result,
friction and evidence at each step. Do not label an entire product verified from
one screen. Motion needs exercised transitions or frames, not an endpoint alone.

Correct supported material defects, inspect their effects and stop on the
acceptance criteria, a user limit or a concrete blocker. No new full audit is
needed after a local repair unless the affected scope warrants it.

## Preview access

Reuse an existing HTTP preview. If none exists and the browser can reach this
machine, serve only the artifact directory on loopback. For a remote browser,
use its supported forwarded URL. Use file navigation only when supported.
Confirm the intended page opened; distinguish preview-access failures from
rendering defects. Do not broaden server exposure to work around access.

## Viewport sweep

Render one page at a fixed set of widths and heights. Measure each render for sideways scroll, clipped text and controls that only hover reveals.

The widths are exact: 320, 375, 768, 1024 and 1440, plus 1px either side of each project breakpoint. A width reasoned from the media queries is a finding. Run it after any layout change and whenever the user names a phone or a width. An untested width remains a coverage gap rather than an implied pass.

1. **Read the breakpoints** from the CSS, the Tailwind config or the tokens. Add 1px below and 1px above each one to the fixed widths.
2. **Render each width** through device emulation. Use 320×568, 375×812, 768×1024, 1024×768 and 1440×900. Breakpoint edges render 800px tall. Emulate touch at every width under 1024. Take a full-page screenshot of each. A layout judged from the code is a finding.
3. **Measure each render.** On the web, run [overflow.js](viewports/overflow.js) through the browser's evaluate call at each width. Treat each result as a candidate until a crop of that width shows it. The page never scrolls sideways, though a box may scroll inside itself. Text is never cut by its box without an ellipsis or a clamp.
4. **Tap at touch widths.** Row actions, copy buttons and menus that appear on hover need another way to appear.
5. **Shorten the height.** Render 812×375, a phone held sideways. Open each dialog, sheet and menu at that size. Content scrolls inside the overlay and its actions stay reachable.

Name the width in every finding.

| Broken | Replacement |
| --- | --- |
| Checked at 375 and 1440 only | Also at 767 and 768, 1023 and 1024 |
| "The grid collapses at `md`, so mobile is fine" | Screenshots at 320, 375 and 768 |
| A `width: 400px` card at 320 | `max-width: 100%` on the card |
| `overflow: hidden` cutting a label at 375 | The label wraps, or truncates with a way back |
| Row actions behind `:hover` alone | Shown at all times under `(hover: none)` |
| A dialog's `Save` below a 375px screen | `max-height: 100dvh` with the body scrolling |
| "The header overlaps" | "At 768, the header overlaps the search field" |

Adapted from Raphael Salaja's public viewports (raphaelsalaja/skills, commit 31031e9);
[overflow.js](viewports/overflow.js) is copied unchanged. See
[license](raphael-salaja-LICENSE.txt).
