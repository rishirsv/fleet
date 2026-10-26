# Components

Load `../assets/base.css`; add `../assets/export.js` only for export controls.
These are ordinary semantic HTML patterns, not custom elements. Exact classes
and tokens live in the stylesheet. Copy a relevant example and remove unused
sections; do not generate the whole catalog on every page.

| Need | Pattern | Working example |
|---|---|---|
| Reading rhythm | `main.stack-lg`, `header.stack`, `section.stack` | [Decision brief](../examples/release-decision.html) |
| Alternatives | `.split` with one `article.stack` per option | Decision brief |
| Evidence values | `dl.facts` with `dt` and `dd` | Decision brief |
| Conclusion | `aside.callout` | Decision brief |
| Diagram | `figure`, `.flow.scroll`, SVG, `figcaption` | Decision brief |
| Editor | `section.panel.stack`, labeled native controls, `.row` actions | Both examples |
| Source with annotations | `.code-review`, `.code-lines`, `.code-line`, `.annotation` | [Annotated code](../examples/annotated-code.html) |
| Diff | `pre > code` with `.added` / `.removed` and explicit + / − markers | Annotated code |
| Structured comparison | `.scroll > table.table`, `thead`, `tbody` | Annotated code |
| Supporting detail | Native `details` and `summary` | Decision brief |

Give scroll containers `tabindex="0"` and a meaningful accessible label when
keyboard users need to scroll them. Code anchors link to real stable line IDs;
annotations retain a finding ID across revisions. Escape source code as text.

## Export helper

`htmlAuthoring.downloadJSON(value, filename)` exports the current data. Catch
errors in the caller if data may be unserializable. It requests a download,
not confirmation that the user saved it.

`await htmlAuthoring.copy(text, fallbackTextarea)` returns true on clipboard
success; otherwise exposes and selects the supplied textarea. Provide a label
and status message in the caller. Keep the current editor values intact.

The examples own their data and event handlers. The helper owns only export
mechanics. An artifact does not need a new state framework, generated component
registry or build project to use these pieces.
