# Typography

Shape how text communicates identity, hierarchy, and meaning. Inspect
established faces, roles, and rendered content before editing. Preserve
confirmed families unless changing the identity is in scope.

## Choose type for the surface

Expressive headlines can carry the subject's character through distinctive
letterforms, proportions, and composition. For sustained reading, make lines
easy to follow. For compact controls, make labels easy to recognize. For data,
make values easy to compare. Tune these uses separately.

A common family can be the right choice; replace it only for a concrete gain.
Add a second family only for a clear role, with enough contrast to make the
pairing intentional.

## Build hierarchy through roles

Define the display, heading, body, label, metadata, and numeric roles the
interface needs. Reuse the project's tokens and keep repeated roles consistent.
Combine size, weight, width, space, and case so visual emphasis matches
importance.

## Tune reading and composition

Tune line width, line height, letter spacing, and paragraph spacing together
with the actual font, language, and content. Short headings often benefit from
tighter line height; multiline text needs room to track between lines. Wider
lines generally need more line height. Inspect light text on dark surfaces
before adjusting weight or spacing.

Use stable role sizes for compact interfaces. Fluid display sizing can support
expansive layouts when its minimum and maximum preserve hierarchy. Tune letter
spacing to text size and letterforms; small uppercase labels and large
headlines have different needs. Use paragraph spacing or indentation, and use
both only for a reason.

## Handle wrapping and overflow

Inspect real copy at the widths where it breaks. Balance short headings when it
improves the composition, and adjust wrapping for descriptions when their final
lines look unbalanced. Keep normal wrapping for sustained reading unless the
result justifies a change.

Allow long URLs, identifiers, and words to break without forcing container
overflow. Keep short labels together only when they still fit at supported text
sizes. Truncate secondary text selectively and provide a reachable full value
when omitted content matters; hover alone fails touch and keyboard users.

Test translated text and mixed-direction content. Set language and direction at
the appropriate content boundary; isolate inserted values whose direction
differs. Let text wrap naturally instead of hard-coding line breaks for one
string or viewport.

## Refine font behavior

Load the real weights and italics the design uses. Synthetic styles can distort
the face, but disabling synthesis without available alternatives can erase
emphasis. Inspect required styles and fallbacks before suppressing it.

Use optical sizing when supported, and compare text and display variants at
their intended sizes. Prefer standard properties such as `font-weight` and
`font-variant-numeric` over raw axis or feature tags. Use custom axes and
OpenType features only when the font supports them.

Use tabular numerals for aligned columns and changing values. Tune underlines
so they stay recognizable without cutting through letterforms. Preserve text
selection except where it interferes with a gesture. Check the rendered effect
before imposing font smoothing.
