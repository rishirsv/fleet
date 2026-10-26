# Interactive prototype

Create a fully interactive prototype with realistic state management and
transitions. Use the existing stack where present; otherwise plain JavaScript
is sufficient when it supports the requested behavior. Include the hover
states, click interactions, form validation, animated transitions, and
multi-step navigation flows that the requested prototype needs. It should
feel like a real working app, not a static mockup.

# Make tweakable

If the user tells you what to make tweakable, do that. If not, pick a few
high-impact values — key colors, a layout variant, a feature flag, headline
copy. Keep the Tweaks panel small and tasteful; hide it completely when Tweaks
is off. Implement controls in the page: there is no injected Tweaks service.

State whether edits survive reload.

# Options

Use this for successive rounds of design options, not as a required layout
for every comparison.

Present multiple design options as a vertical stack of turns — each turn of
options is its own `<section>`, newest turn at the **top**, and every option
gets a stable `{turn}{letter}` id (`1a`, `1b`, `2a`…) that the user references
back in chat and you cross-link between turns.

**How to write it** — put one `<style>` block in `<head>`, then one
`<section class="dv-turn">` per turn in the document body. When the user asks
for another round, **insert the new section ABOVE the existing ones** so the
latest work sits at the top; never reorder, renumber, or delete earlier turns
unless the user requests it.

**Rules:** turn section ids are `t1`, `t2`, `t3`…; option ids are `1a`, `1b`,
`2a`… and go on the option's **outermost** element (`.dv-opt`), never on the
badge — so `#1b` scrolls the whole option into view. Ids are stable forever,
never reused or renumbered. Options within a turn sit side-by-side in a
wrapping row. Every option-id reference in the file is an anchor link to
that option; in chat replies, just write `1b`. Size each option to its
content; don't use `height:100%`.

Ordinary browser layout replaces Claude's `<helmet>` and canvas mode. Do not
assume host-provided pan/zoom or build a canvas engine just for option cards.

# Artifact runtime capabilities

A standalone page has no injected `window.claude` APIs or access to this
agent's connectors. Before implementing live data, shared storage, model
calls, or collaborative editing, inspect the actual destination's supported
APIs. A tool available to the agent is not automatically callable by the page.

## Where a page keeps its state

- A per-viewer convenience (a remembered tab, a draft): browser storage; it
  never reaches other viewers or the agent. Wrap reads/writes in try/catch and
  render correctly without storage.
- A task-specific editor: keep current values in memory, with explicit export
  for the agent or user to apply. Browser storage may retain a local draft.
- Shared records or live connected data: use an existing, authorized backend
  or the destination's documented runtime. Do not substitute localStorage
  for shared persistence or introduce a backend for a static document.

For asynchronous features, render the page before connections resolve and
handle unavailable, loading, empty, failed, and read-only states. Keep secrets
out of page source. Learn tool arguments from schemas and results from safe
reads; do not invent a connector contract or execute a write to discover it.

For persistence or collaboration, check read-back through the actual browser/API
runtime; a screenshot alone cannot establish that data was saved or shared.
