# Craft floor

Read before UI edits outside `$design` and during finish review. Enforce the
[generic defaults](../skills/design/SKILL.md#generic-defaults) and the bans
below on authored or reworked UI; do not remove them from the review as mere
taste preferences. Direct user instructions, faithful recreation of an accepted
target, and an explicit incumbent design-system requirement take precedence.
Record that specific authority for an exception; a builder's preference is not
authority. Leave unrelated existing UI alone. Native platform controls and
system text remain native.

## Bans beyond the generic defaults

- No repeated icon/title/body cards used as the whole page's organizing idea. Use the content's relationships to choose the structure.
- Load the actual weights of every face used. Do not tighten letter spacing
  below -0.04em to force a fit.
- No emoji or Unicode symbols substituted for a coherent icon family.
- No handmade vector illustrations, fake grain, faux bevels, or gradients
  standing in for promised photographic, painted, or dimensional assets.
  Produce the actual material. Vector geometry, diagrams, icons, and genuine
  shader effects are valid media; pretending they reproduce a picture is the
  failure. Do not hide required imagery under washes or near-zero opacity and
  count it as delivered.
- No routine bounce or elastic motion. Keep content visible before motion and
  make any expressive motion belong to the chosen direction.

## Check the rendered result

Keep the brief's distinctive composition, type character, material, and color
temperature intact. Match real imagery and font assets instead of approximating
them. Check the first viewport, content density, grouping, and main action at
the relevant sizes. Fix overflow and missing states through the existing
evidence workflow. Invent no commercial claims; mark synthetic demonstration
content honestly.

These checks share the normal inspection captures. They need no separate
detector, engine, config, or checklist artifact. A clean floor is a minimum;
it does not establish that the design achieves the brief.

Informed by Paul Bakaus's Impeccable
craft floor (pbakaus/impeccable, commit 4281ac2)
and finish reviewer (pbakaus/impeccable, commit 4281ac2).
