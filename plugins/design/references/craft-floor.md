# Craft floor

Read before UI edits and during finish review. Enforce these bans on authored
or reworked UI; do not remove them from the review as mere taste preferences.
Direct user instructions, faithful recreation of an accepted target, and an
explicit incumbent design-system requirement take precedence. Record that
specific authority for an exception; a builder's preference is not authority.
Leave unrelated existing UI alone. Native platform controls and system text
remain native; the display-type rule below concerns expressive visual identity.

## Aesthetic bans

- No decorative kicker or eyebrow above a heading. Remove the extra label;
  retain functional breadcrumbs and labels that communicate necessary state.
- No nested cards, or repeated icon/title/body cards used as the whole page's
  organizing idea. Use the content's relationships to choose the structure.
- No stock big-number hero with supporting statistics as a substitute for the
  subject. Real data displays must serve the user's task.
- No section numbering unless order conveys meaning, technical-looking
  monospace without code/data/measurement, or dashboard ornaments without data.
- No gradient-filled text, decorative glass/blur, colored glow halos, or
  colored side borders thicker than 1px on cards, rows, alerts, and callouts.
- No sharp offset block shadows outside a deliberately neobrutalist direction.
  Avoid doubling a container's elevation with both a border and a broad shadow;
  reserve pill shapes for compact controls.
- No Arial, Inter, platform sans, Impact, or Arial Black chosen by default as
  the expressive display voice. Use a face suited to the intended lettering
  and load its actual weights. Do not tighten web letter spacing below -0.04em
  to force a fit.
- No emoji or Unicode symbols substituted for a coherent icon family. Use a
  consistent library or deliberately drawn icons.
- No handmade SVG illustrations, fake grain, CSS bevels, or gradients standing
  in for promised photographic, painted, or dimensional assets. Produce the
  actual material. SVG geometry, diagrams, icons, and genuine shader effects
  are valid media; pretending they reproduce a picture is the failure.
- No geometric approximation of a subject's organic silhouette. Use a real
  cutout or mask derived from the image. Do not hide required imagery under
  washes or near-zero opacity and count it as delivered.
- No decorative background grids, stripes, or textures without a connection to
  the chosen subject and visual direction. Choose light/dark from the use
  environment rather than a category stereotype.
- No routine bounce/elastic motion, identical fade-up entrances on every
  section, or hover lifts on every card. Keep content visible before motion
  and make any expressive motion belong to the chosen direction.
- No modal for work that needs neither interruption nor protected focus.
- No neutral-gray secondary text on colored surfaces; derive it from the
  foreground or surface hue and verify contrast.
- No default purple-to-blue gradient palette or pure black/neutral-gray surface
  scheme. Choose hues from the subject and tint light and dark surfaces.

## Check the rendered result

Keep the brief's distinctive composition, type character, material, and color
temperature intact. Match real imagery and font assets instead of approximating
them. Check the first viewport, content density, grouping, and main action at
the relevant sizes. Fix overflow and missing states; verify contrast, keyboard
focus, and reduced motion through the existing evidence workflow. Invent no
commercial claims; mark synthetic demonstration content honestly.

These checks share the normal inspection captures. They need no separate
detector, engine, config, or checklist artifact. A clean floor is a minimum;
it does not establish that the design achieves the brief.

Informed by Paul Bakaus's Impeccable
[craft floor](https://github.com/pbakaus/impeccable/blob/4281ac224087af05d4d9f0ab20c16a62a345493e/skill/reference/craft-floor.md)
and [finish reviewer](https://github.com/pbakaus/impeccable/blob/4281ac224087af05d4d9f0ab20c16a62a345493e/skill/agents/impeccable-finish-reviewer.md).
