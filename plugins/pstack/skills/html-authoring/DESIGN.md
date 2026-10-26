# HTML authoring design system

A working document should make evidence easy to inspect and decisions easy to
return. Use this default when the user or project has not supplied a visual
system. It applies to briefs, explainers and small editors; a prototype of an
existing product inherits that product's appearance.

## Foundation

[base.css](assets/base.css) owns exact token values, responsive behavior and
component styles. Change values there, not in this document or each example.
Use system sans for reading and controls, monospace for code and aligned data.
Hierarchy comes from size, weight, position and space. Display typography is an
explicit editorial choice, not a requirement.

Use a white canvas, cool neutral surfaces and blue for actions and selection.
Dark mode retains the same hierarchy with its own tokens. Success, warning and
error colors express state; pair them with words or diff markers. Do not use
color alone to distinguish meaning.

## Composition

- Reading text stays near the reading-width token. Comparisons, code and
  diagrams can occupy the wider page. Keep their overflow inside the figure.
- Open with the subject and the useful conclusion or action. Skip decorative
  eyebrows, giant heroes and repeated explanations of what the interface does.
- Use open sections for the argument. A panel groups a bounded editor or tool;
  a callout highlights a conclusion. Do not put every section in a card.
- Use a comparison grid for alternatives, a table for matching attributes,
  and a diagram for mechanisms. These are composable parts, not page templates.
- Place annotations beside source on wide screens and below it on narrow ones.
  Give code lines and findings stable anchors. Preserve file/revision context.
- Use anchors for navigation, disclosure for supporting detail, and tabs only
  for genuinely alternative views. Never hide the primary argument by default.

## Interaction

Use native controls with visible labels and focus. Keep the user's edits in
memory unless persistence is requested. Put export beside the work it captures;
export real values, stable identifiers and enough context to interpret them.
Use explicit action names. Announce success or failure without replacing the
user's work. If copying is unavailable, expose selectable text. Downloading
requests a browser download; it does not prove the file was saved.

## Editing and delivery

Author plain HTML with linked local CSS and optional JavaScript. Reuse the
components shown in [the examples](references/components.md); copy only what
serves the task. Keep content in HTML and behavior in ordinary named functions.
No component registry, package installation or runtime is required.

For a localized follow-up, edit the smallest relevant region and preserve the
rest of the document. Keep element IDs stable. Broad rewrites are appropriate
when the requested composition changes, not for a text or color adjustment.

For a portable file, run `python3 scripts/export_html.py INPUT OUTPUT` from this
skill directory. It embeds local stylesheets and scripts, checks common unresolved
resource references, and leaves the editable source intact. Output must be a
separate file. This is a packaging helper, not a general HTML or JavaScript validator.
The exporter does not fetch assets or run a browser; use embedded
images or the existing project's bundler for richer assets.

Inspect the actual exported page. The skill entrypoint owns browser checks;
this system adds no separate review loop or file-size ceiling.
