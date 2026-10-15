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

## Preview and viewport checks

Reuse an existing HTTP preview. If none exists and the browser can reach this
machine, serve only the artifact directory on loopback. For a remote browser,
use its supported forwarded URL. Use file navigation only when supported.
Confirm the intended page opened; distinguish preview-access failures from
rendering defects. Do not broaden server exposure to work around access.

Include a narrow viewport for responsive work, and use 320px when supported or
requested. Check affected breakpoints and unintended horizontal overflow;
wide content should scroll within its own container. An untested width remains
a coverage gap rather than an implied pass.
