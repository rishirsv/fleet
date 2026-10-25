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

Choose the supported format for the explanatory job: native prose and tables
for reading and lookup, Mermaid for sufficient simple relationships, and the
Page Visualize workflow for custom diagrams, charts, and simulations, even when
no interaction is needed. Read the full Visualize guidance and current Page
content contract; use the Page-specific insertion workflow, not the chat output
contract. Keep source inspectable rather than defaulting custom graphics to PNG.
Use uploaded images for art or when a static fallback is actually needed; verify
both insertion and rendering. Do not rasterize prose, code, or tables for style.

Keep graphical exhibits compact, theme-aware, and responsive to their actual
container width. Use host typography, restrained semantic hierarchy and
connectors, and readable labels rather than shrinking a desktop canvas. Keep
article prose, takeaways, and sources native outside the exhibit.

Use interaction when it lets the reader investigate a meaningful question.
Define the data or rules, control, visible consequence, useful initial example,
and limits before building. A stepper can reveal dangerous ordering; a selector
can expose effects an average hides. More controls are not inherently more
ambitious. For simulations, test transitions and derived values against the
stated model, including boundaries and failure states; compare reachable states
and paths when claiming equivalence to an executable model. Label hypothetical
inputs and do not imply that model agreement proves production behavior.

When host compatibility is uncertain, test one scoped prototype before rollout.
Distinguish static HTML rendering, custom JavaScript behavior, and required CDN
loads: success in one does not prove the others. Inspect the saved Page at wide
and phone widths and in relevant themes; test meaningful controls, keyboard and
touch behavior, reduced motion, and supported state persistence without
replacing collaborator state with defaults. Source, upload, or isolated script
tests do not establish host support. Chat widgets do not establish Page portability.
Do not diagnose a failed embed or reject all HTML from one failure.

Fix and retest a supported exhibit when feasible. If required capabilities fail
or cannot be verified, use precise static figures and native text covering the
important states, and disclose the verification limit. Remove failed embeds and
obsolete control instructions within the authorized scope. Preserve unrelated
content and provide useful text alternatives for important graphical states.

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
