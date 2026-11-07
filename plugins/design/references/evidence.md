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

## Web preview access

Reuse an existing HTTP preview. If none exists and the browser can reach this
machine, serve only the artifact directory on loopback. For a remote browser,
use its supported forwarded URL. Use file navigation only when supported.
Confirm the intended page opened; distinguish preview-access failures from
rendering defects. Do not broaden server exposure to work around access.

## Viewport sweep

Render one screen at a fixed set of sizes. Measure each render for sideways scroll, clipped text and controls that only hover reveals.

The sizes are exact: the smallest and largest supported, a common middle size, and 1pt either side of every point where the layout changes (a breakpoint or a size-class change). A size reasoned from the layout code is a finding. Run it after any layout change and whenever the user names a device or a size. An untested size remains a coverage gap rather than an implied pass.

1. **Read the layout edges** from the breakpoints, size classes or tokens. Add 1pt below and 1pt above each one to the fixed sizes.
2. **Render each size** in a simulator, preview or device emulation, with touch at phone and tablet sizes. Capture the whole screen at each. A layout judged from the code is a finding.
3. **Measure each render.** Treat each automated result as a candidate until a capture at that size shows it. The screen never scrolls sideways unless it is designed to, though a region may scroll inside itself. Text is never cut by its box without an ellipsis or a clamp.
4. **Tap at touch sizes.** Row actions, copy buttons and menus that appear on hover need another way to appear.
5. **Shorten the height.** Render a phone held sideways. Open each dialog, sheet and menu at that size. Content scrolls inside the overlay and its actions stay reachable.

Name the size in every finding.

| Broken | Replacement |
| --- | --- |
| Checked at one phone and one desktop size only | Also 1pt either side of each layout edge |
| "The grid collapses at the compact size, so phones are fine" | Captures at the smallest phone, a common phone and a tablet |
| A fixed-width card at the smallest size | The card's width follows its container |
| A label cut by its box | The label wraps, or truncates with a way back |
| Row actions behind hover alone | Shown at all times on touch |
| A dialog's `Save` below a landscape phone screen | The dialog body scrolls and its actions stay visible |
| "The header overlaps" | "At 768, the header overlaps the search field" |

**On Apple platforms**, the sizes are the smallest and largest supported iPhone, each in landscape, and on iPad the narrowest multitasking widths the app supports. The layout edges are the compact and regular size-class changes.

**On the web**, the widths are 320, 375, 768, 1024 and 1440 at 320×568, 375×812, 768×1024, 1024×768 and 1440×900, with breakpoint edges 800px tall, touch emulated under 1024, and 812×375 for the short height. Read breakpoints from the CSS, the Tailwind config or the tokens, and run [overflow.js](viewports/overflow.js) through the browser's evaluate call at each width. Fixes are usually `max-width: 100%`, visibility under `(hover: none)`, and `max-height: 100dvh` with the body scrolling.

Adapted from Raphael Salaja's public viewports (raphaelsalaja/skills, commit 31031e9);
[overflow.js](viewports/overflow.js) is copied unchanged. See
[license](raphael-salaja-LICENSE.txt).
