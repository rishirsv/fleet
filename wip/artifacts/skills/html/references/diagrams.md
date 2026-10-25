# Diagram vocabulary

Use this to choose a diagram form and the helper or gallery figure that draws
it. For page modules, use the `flow`, `state`, `sequence`, or computed
`timeline` helper when it fits; `node scripts/catalog.mjs --help <helper>`
shows the input shape. Use [the diagram gallery](../assets/diagrams.html) to
compare visual forms. Hand-author a figure when the helpers cannot express the
relationship or the composition needs precise placement.

## Choose by the question

| Reader question | Diagram | Atlas source |
|---|---|---|
| What parts exist and how do they connect? | Architecture | `#architecture` |
| How does the full system divide into layers, paths, and owners? | Architecture board | `#architecture-board` |
| What did a change remove, add, or keep in a system? | Architecture delta | `#architecture-delta` |
| What happens at each decision branch? | Flowchart | `#flowchart` |
| Where do items sit on two independent axes? | Quadrant | `#quadrant` |
| Which categories are larger or smaller? | Bar chart | `#bar-chart` |
| How does a measure change over time? | Line chart | `#line-chart` |
| How does a whole divide into a few parts? | Donut chart | `#donut-chart` |
| Which states exist and what transitions between them? | State machine | `#state-machine` |
| When did milestones happen? | Timeline | `#timeline` |
| When does each task run, and what blocks what? | Gantt | `#gantt` |
| How does work cross roles or systems? | Swimlane | `#swimlane` |
| What is the parent-child hierarchy? | Tree | `#tree` |
| Which causes produced one incident or effect? | Fishbone | `#fishbone` |
| Which modules depend on which, and where is the cycle? | Dependency graph | `#dependency-graph` |
| Which layers sit above or depend on others? | Layer stack | `#layer-stack` |
| Where do two or three sets overlap? | Venn | `#venn` |
| How did an open-high-low-close series move? | Candlestick | `#candlestick` |
| Which increments and decrements explain the ending value? | Waterfall | `#waterfall` |
| Where does a measure concentrate across two categories? | Heatmap | `#heatmap` |
| What messages pass between participants over time? | Sequence | `#sequence` |
| What fields, methods, and inheritance define the types? | Class | `#class` |
| Which records relate, and with what cardinality? | Entity relationship | `#entity-relationship` |

Use a comparison table for a binary contrast when exact criteria matter.
For a plan, use a flow for phases or decisions, a sequence or swimlane for
owners and handoffs, or a timeline or Gantt for supplied dates and dependencies.

## Make the relationship clear

- Keep an embedded diagram to about 4–9 nodes. Split a larger explanation into
  two diagrams or use an architecture board.
- Emphasize only one or two elements. Neutral structure should
  occupy most of the drawing.
- Remove connectors whose meaning is already obvious from placement.
- When capture flags shrunken SVG labels, move important labels into HTML or
  let the figure scroll in its wrapper.
- State the equivalent relationship in an adjacent summary or ordered
  explanation.
- Use existing tokens. New diagrams can use different geometry. Preserve
  the palette, fonts, flat unshadowed shapes, and absence of decorative texture.

For bar, line, donut, candlestick, waterfall, and heatmap forms, also read
[charts.md](charts.md). Exact values need visible labels or an adjacent table;
the picture is not the only copy of the data.

## Architecture boards

Use an architecture board only when one embedded figure cannot show the
system boundary, principal runtime path, intervention point, and ownership
together. Organize it into a stable reading order:

1. title and judgment;
2. external roles or business domains;
3. system modules;
4. runtime or data path;
5. governance, ownership, or next intervention.

Prefer bands with dividers over a field of small cards. Keep 10–25 major
blocks. If more blocks are needed, group details by domain. Orthogonal connectors should
not cross text or run along a module border.

## Hand-authored figures

Each gallery example is a complete `<figure>` with inline SVG and an adjacent
text summary. For a form without a computed helper, copy the closest figure,
then replace the example labels, values, connectors, and summary with the
supplied material. In a page, pass the SVG to `flowDiagram()`, which ships the
shared `.diagram-*` rules with the `flow-diagram` component.

Draw at 1:1: set the viewBox width to the space the figure gets (about 840 in an
article page) and `minWidth` to the same value, so narrow screens scroll the
figure instead of shrinking its labels. Use the shared grammar so every figure
reads the same way:

- nodes: `.diagram-node` rectangles with 6px corners, 36px tall, or 52px with a
  `.diagram-label.is-small` sublabel; `is-store`, `is-external`, `is-added`,
  and `is-removed` mark node kinds;
- connectors: 1px `.diagram-edge` paths that turn at right angles with
  rounded 8px elbows; `is-async` dashes them;
- labels: `.diagram-label` for names, `.diagram-tag` (monospace capitals, at
  most about 16 characters) for connector, axis, and group labels;
- groups: `.diagram-region` panels with a tag in the top-left corner;
- coordinates on a 4px grid, with at least 24px between nodes.

Inspect each diagram at its actual display width. Fix overlapping labels,
ambiguous crossings, clipped content, unreadable scaled text, and strong
emphasis on more than two elements.
