# Ideation

Explore distinct directions through local HTML prototypes, native previews, or
generated images. Reuse the settled brief; ground the design first when the
subject, audience, or intended outcome still needs clarification.

## Contents

- [Frame the exploration](#frame-the-exploration)
- [Choose the medium](#choose-the-medium)
- [HTML variants and board](#html-variants-and-board)
- [Image variants](#image-variants)
- [Content fixtures and tuning panels](#content-fixtures-and-tuning-panels)
- [Compare and continue](#compare-and-continue)

## Frame the exploration

Identify the decision the variants should resolve: the product's purpose,
information hierarchy, composition, interaction, or visual identity. Inspect
relevant product screens and supplied references directly. Preserve the brief's
hard constraints and distinguish missing evidence from freedom to invent.

For an established product, vary structure, emphasis, and interaction within its
identity unless a new style is requested. For broad exploration, vary both
concept and visual system. Give each direction a descriptive name and briefly
explain its main idea. Make differences that change the experience; a change in
accent color alone is insufficient.

Default to three variants unless the user specifies a count or the question
needs a smaller comparison. Keep subject, core content, task, and viewport
comparable so the user can judge the intended differences. Producing three
alternatives is one exploration round, separate from the iteration count.

## Choose the medium

- **HTML prototypes:** default for web questions about layout, typography,
  responsiveness, or interaction. Build only enough behavior to experience the
  meaningful difference.
- **Native previews:** use the target stack for platform controls, gestures,
  text scaling, or spatial behavior. Keep named variants and reusable preview
  states; compare them in the native preview environment and retain the
  selected source.
- **Image generation:** use for rapid visual direction, imagery, or
  compositions whose expression is easier to explore as images. Treat
  generated controls as visual proposals; they show no working behavior.
- **Mixed:** use images for art direction or assets and HTML for the interaction
  question. Keep the extra medium only when it helps decide.

Follow an explicit medium preference. Choose dimensions from the reference or
intended surface; use consistent viewports across comparable options instead of
forcing every concept into one device preset.

## HTML variants and board

Create isolated local HTML variants with stable names and paths. Reuse existing
prototype or board conventions when available. Otherwise create a local HTML
comparison board linking to each variant, with embedded previews at the same
viewport and an option to open each at full size. Give the board plain, neutral
chrome so it does not compete with the variants; it follows no style system.

Keep titles, descriptions of each direction, and comparison notes outside the
prototype viewport. Let users inspect each design at its intended scale; a
thumbnail cannot establish readability. Show the main task with realistic
content, the distinguishing interaction, and relevant states. Use local sample
data and assets instead of adding backend services for an exploration.

Open the board and variants in the browser. Check that previews load, primary
interactions work, and the board does not alter the designs' layout or scale.
Preserve the individual artifacts so later feedback can name a specific variant.

## Image variants

Create each direction as a separate image. Attach relevant visual references
through the available image tool and include product tokens or constraints in
the prompt. Claim a reference was attached only when the tool received it. If a
required reference is inaccessible, resolve that gap; otherwise disclose what
the proposal could not use.

For each prompt, specify:

- Subject, audience, primary job, and what makes the direction distinct.
- Intended viewport or aspect ratio and the screen or state to depict.
- Realistic content, hierarchy, palette, typography, and asset treatment.
- Existing design constraints and the aspects intentionally being varied.

Show the intended task, leaving out features that do not help explain the
direction. Use grouping, spacing, and typography to establish hierarchy; add
containers and decoration where they serve the direction. Keep device chrome
outside the design unless it is part of the requested presentation. Preserve
source dates or use a coherent date context when temporal content matters.

Present each generated result once and record its exact result identifier. When
numbering options, number them in their displayed order after results appear.
Use stable concept names and result identifiers so later selection remains
unambiguous.

## Content fixtures and tuning panels

Keep named preview states for realistic, empty, crowded, and unusually long
content. Reuse editable fixtures so a content change can be compared across
variants. Generated fixtures find design weaknesses; feedback from people who
use the product shows their needs and experience.

When several parameters interact, build a temporary tuning panel beside the
preview. Name the animation phases and expose only the values under comparison.
Preserve the selected values in the implementation and remove the panel from
product UI unless the user requested it as a feature.

## Compare and continue

Show the variants with a short comparison of their defining choice, benefit, and
trade-off. Recommend the direction that best meets the brief and explain why.
Judge each option against the brief instead of a single aesthetic preference.

For ideation-only requests, stop with the reviewable options and ask which to
pursue or refine. If the user already asked you to choose and build, select the
direction best supported by the brief and evidence and continue. Do not add a
second confirmation after an unambiguous selection.

Apply feedback to the named variant. When combining directions, identify which
structure, styling, and behavior to retain; produce a revised concept if you
need to show how the combined elements will look. Small, explicit corrections
can go directly into the selected HTML prototype. Preserve earlier variants for
comparison.

Continue from the selected prototype source instead of rebuilding it. For a
selected image, follow the recreation workflow. Once an accepted visual target
exists, design QA governs fidelity and correction iterations; ideation needs no
fidelity pass before a target is chosen.
