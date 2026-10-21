---
name: editorial-pages
description: "Creates or improves visually rich native ChatGPT Pages with sustained prose, art-directed images, and explanatory figures. Use for editorial explainers or visual-reference adaptations, not ordinary notes, standalone HTML, or product UI."
---

# Editorial Pages

Compose an editable article, not a dashboard with paragraphs between cards.
Use this skill for native ChatGPT Pages. Use the existing HTML workflow when
the requested deliverable is a browser-openable document, and product design
guidance for an application interface. Do not silently substitute one format
for another when Page tools are unavailable.

Follow the active Page tools' authoring, upload, and mutation contracts. This
skill owns editorial composition and its quality checks, not a second tool API.

## Preserve the source and destination

Read the supplied material and the intended Page before writing. When a visual
reference is supplied, inspect its rendered appearance when accessible and its
source and assets when available. Read representative prose, not only headings.
Distinguish observed appearance from behavior inferred from source.

Keep the visual reference separate from the subject being explained. Preserve
the source's causal chain, useful specifics, qualifications, and citations.
For an adaptation, inventory each meaningful visual, decision or interactive
state, code example, table, and prose function, then map each to its Page
counterpart. Preserve explanatory coverage and sequence; justify substitutions
from observed evidence rather than silently dropping mechanisms. Keep native
text and comparisons native where they serve the same function.

Reuse the identified destination rather than making a Page for each revision.
Replace content only within the authorized scope; a comparison or throwaway
label does not override an access denial. Preserve unrelated blocks, parentage,
Space placement, and sharing. Do not move, archive, delete, or duplicate other
Pages merely to make the workspace look cleaner. Check authorization before
uploading assets whose use depends on replacing protected content.

## Shape the article

Start from a central tension and a concrete example. Let the reader encounter
the mechanism before introducing its terminology or tool taxonomy. Name the
question a visual resolves, show one compact mechanism, then immediately explain
what the reader should infer. Use this sequence where prose alone obscures
ordering, ownership, comparison, composition, or consequences, not as a template
for every section. Compactness applies to each visual, not to the number of
ideas preserved. Do not impose an arbitrary diagram-count cap.

Keep titles, headings, and captions native and editable. Keep definitions,
instructions, qualifications, sources, code, and ordinary
comparisons in native prose, code blocks, or tables. Use a diagram for the
relationship that is hard to see in that text, not to turn the text into a poster.
Preserve the source's nuance while choosing the simplest form for each idea.

Choose a subject-specific visual idea and a coherent medium, palette, recurring
objects, and composition. Use visuals for distinct purposes: establish a scene,
explain a mechanism, compare alternatives, or resolve the opening question.
Avoid consecutive poster-sized figures; alternate compact visuals with their
interpretation and deeper prose. Keep prose at reading width; widen selected
art or figures only through supported layout
metadata, preserving their geometry.

The host controls native typography and page styling. Do not promise custom
fonts, paper colors, sticky navigation, or arbitrary columns that it cannot
provide. Do not hide the whole article in HTML, an iframe, or a screenshot to
imitate that styling. Preserve the editable outline and reading experience.

## Make visuals truthful

Use image generation for a useful scene or conceptual metaphor. Specify the
idea, composition, aspect ratio, medium, and palette; inspect the result and
revise weak compositions. Use supplied or sourced images when identity or
documentary evidence matters. Distinguish illustrations from evidence where a
reader could confuse them, and preserve credits without inventing attribution.

Keep article text out of generated images. Produce precise diagrams and labels
with deterministic rendering, not generated typography. Derive values and marks
from the same data and keep material assumptions beside the claim. Label a
bounded model, hypothetical example, or analogy as such; do not invent measured
values or use decorative precision.

For static diagrams, default to native uploaded figures with native captions.
Do not rasterize prose, code, or tables merely to make them look designed.
Confirm the upload's accessible reference, insert it, and read back the saved Page. An
uploaded file alone is not an inserted figure. Make important facts and states
available in native text, with useful image descriptions where supported.

Use interaction only when it answers a question materially better than a static
figure. Define the question, data or rules, control, visible consequence, initial
state, and limits before building. A stepper can reveal a dangerous ordering;
a selector can expose effects an average hides. A static contrast rarely needs
controls. Keep article prose and sources outside the exhibit.

Do not deliver an interactive exhibit until the saved Page has been observed
rendering it and its meaningful controls have been tested in the actual host.
Chat widgets are not evidence that the same component works in Pages. Do not
claim source portability or diagnose a failed embed without evidence. A failed
embed does not establish that all interaction is unsupported.
Source, upload, or isolated JavaScript tests do not establish host support.
If host verification fails or is unavailable, use precise static figures and native
text covering the important states instead. Remove failed embeds and obsolete
control instructions within the authorized scope. Preserve unrelated content.
For verified interactions, check keyboard use, narrow layouts, reduced motion,
and supported state persistence without overwriting collaborator state on load.

## Verify the saved article

Read back the saved Page and check substantive coverage, citations, figure
references, order, and captions. Reconcile the adaptation inventory against the
saved Page: each source function and meaningful state needs a counterpart or an
explicit, justified substitution. Readability alone is not coverage.
Check that code, diagram transitions, captions,
and stated assumptions describe the same mechanism, including atomic steps and
failure conditions. Preserve correctness as a gate before interpreting a speed
or cost comparison. Inspect the actual saved rendering at wide and
narrow widths when accessible, including the opening, prose-to-visual transitions,
and ending. Check for weak art, repetitive cards, clipped labels, unreadably
scaled figures, redundant headings, and missing context. Check that each visual
answers its setup question and its following prose explains the consequence.
Fix observed defects and inspect the affected section again; a rendering pass
from an earlier version does not validate revised figures or prose.

At the target phone width, read the labels at the displayed size without zooming.
An image loading or fitting without clipping is not a readability pass. If labels
are too small, simplify or stack the figure and inspect the saved result again.
Check native code for broken identifiers or lost indentation and tables for
unreadable word breaks; reflow them without changing their meaning.

Report the Page link, what improved, and material limitations. Distinguish source
inspection, saved-content checks, actual rendering, and tested interaction.
If narrow or mobile rendering was not observed, say so; desktop readback is not
mobile proof. Do not claim an exact visual replica or a fully verified article
without the corresponding evidence.
