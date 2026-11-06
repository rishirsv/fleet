# Typography

Shape how text communicates identity, hierarchy, and meaning. Inspect
established faces, roles, and rendered content before editing. Write every fix
in the project's own styling system or text styles.

Sizes are in points: CSS `px` on the web, `pt` on Apple platforms. The words
belong to the [UX-copy guide](../../../references/ux-copy.md) and spatial layout
to [Layout](layout.md). Contrast belongs to [Color](color.md).

## Measured, not preferred

Some values here are exact. Line-height that scales with size, weight `400` or heavier below `18pt`, a 60–75 character measure and fixed-width digits on changing values are findings when missed.

Letter-spacing, pairing and scale ratios are heuristics. Report them only where they break the project's own scale. Never propose a new typeface, paid or free, unless the task asks for a type change.

## Choose type for the surface

Expressive headlines can carry the subject's character through distinctive
letterforms, proportions, and composition. For sustained reading, make lines
easy to follow. For compact controls, make labels easy to recognize. For data,
make values easy to compare. Tune these uses separately.

## Fewer fonts, sizes and weights

Rarely use more than three fonts; marketing pages can carry more than apps. Weight and size carry hierarchy, so each extra one dilutes it. Pair for contrast. A serif headline over a sans body reads as deliberate, two near-identical sans-serifs read as a mistake.

Below `18pt`, use weight `400` (regular) or heavier. Weights `100`–`300` belong at `28pt` and up, checked against the background even there. Categories, `Display` and `Text` cuts and fallbacks are in [choosing-fonts.md](typography/choosing-fonts.md). Monospace inside running text drops to `0.9×` the surrounding size, so inline code doesn't tower over its sentence.

## Ship the faces the design uses

When a family lacks a weight or style, the renderer synthesizes one and distorts the face. Ship every weight and style the design uses. Disable synthesis only after checking the fallback, and only for the unwanted mode.

## Typed font settings over raw tags

Set weight, numeric style and optical size through the platform's typed font settings, not raw OpenType tags; typed settings keep working when a fallback font renders. Leave optical sizing automatic unless the design deliberately decouples it from size. Reserve raw tags for custom axes and features with no typed setting, such as a stylistic set. Axes and features are in [variable-fonts-and-opentype.md](typography/variable-fonts-and-opentype.md).

## Use a type scale with semantic names

Define a small set of sizes and deviate from it as little as possible. Pair each size with its line-height and weight, so a role is one decision instead of three. Prefer the platform's text styles where they exist, so text follows the reader's size setting.

Solo, default names are fine when the usage rules are clear. On a team, name sizes by use (`body-sm`) so the rules survive other people. A [role-based starting scale](typography/spacing-and-sizing.md#type-scale) is in the reference.

Fluid display sizing can support expansive layouts when its minimum and maximum
preserve hierarchy.

## Heading sizes descend with level

Map heading levels to descending steps of the scale, so a subordinate heading never overpowers its parent. Deep levels may share a size where the scale runs out of steps, as long as weight or letter-spacing keeps them distinct. A heading is never smaller than body text unless it is a deliberate overline. See the [level mapping](typography/spacing-and-sizing.md#heading-hierarchy).

## Line-height by role

Display text `1.1`, headings `1.2`–`1.3`, body copy `1.5`–`1.6`, as multiples of the font size. Express line-height relative to size so it scales when the text does; a fixed height does not.

Tight line-height is for short text. Anything that wraps to three or more lines needs at least `1.4`, even in a height-constrained row. See the [card description example](typography/spacing-and-sizing.md#line-height-for-wrapping-text).

Use paragraph spacing or indentation, and use both only for a reason.

## Letter-spacing by size

Headings at `24pt` and up take `-1%` to `-2%` of the size. Uppercase labels at `14pt` or smaller take `5%`. Body copy stays at `0`. Express tracking relative to size so it scales.

Kerning is built into the font and on by default. Turning it off is never a fix.

## Cap the measure

Cap long-form text at 60–75 characters per line. Any unit works, as long as a cap exists and the line length lands in range, including on wide windows and iPad. See [unit choices](typography/wrapping-and-punctuation.md#measure-line-length).

## Wrap deliberately

Inspect real copy at the widths and text sizes where it breaks.

- Balance short headings and descriptions so lines are even. Never balance paragraphs.
- Keep a lone word off the last line of a paragraph where the platform supports it.
- Let a long word, link or ID break rather than escape its container, and let the container shrink in a row.
- Keep short labels and badges on one line where a break looks broken, as long as they still fit at supported text sizes.

Align interface text to the leading edge. Justify only in specific editorial layouts. Let text wrap naturally instead of hard-coding line breaks for one string or width.

## Fixed-width digits on changing values

Use fixed-width (tabular or monospaced) digits for timers, counters, prices and numeric table columns, so every digit keeps one width and nothing shifts. Leave figures in prose proportional.

## Truncate with a way back

A truncated value needs a way back to the full text when omitted content
matters; hover alone fails touch and keyboard users.

Every long string forces this choice. Make it per field, not globally:

- **Wrap** text the user needs in full to identify something: names, titles in a detail view. Two lines is usually fine; four is a sign the column is too narrow.
- **Truncate at the end** for secondary metadata where the start carries the meaning: role, description, last message preview.
- **Truncate in the middle** when items differ at the *end*: file names (`Q3-report…v12-final.pdf`), emails sharing a long domain, paths, hashes. End-truncation makes them identical.
- **Clamp** to a fixed line count for multi-line previews in cards, so card heights stay predictable.
- **Never truncate** numbers, amounts, dates, or anything the user compares. Give them the room.

## Natural case, typographic punctuation

Store text in natural case and apply case in styling, so a redesign never means rewriting copy.

Rendered text uses typographic characters, never their keyboard stand-ins. Curly quotes, en dashes, the ellipsis character and non-breaking spaces are in the [substitution table](typography/wrapping-and-punctuation.md#smart-punctuation). Code keeps straight quotes.

## Underlines from the font

Use the font's own underline position and thickness, or tune offset and thickness by hand. A dotted underline hints that a word carries extra information, such as an abbreviation or a defined term.

Color is the only part of a real underline that animates reliably. Any other underline animation needs a separate element, and its motion follows [Motion](motion.md).

## Respect the reader's text size

Set sizes in units that follow the reader's text-size setting: Dynamic Type text styles on Apple platforms, `rem` on the web. Check the largest supported setting as well as the default.

Start long-form body text at the platform's default reading size (`17pt` body on iOS, `16px` on the web). Move off it only for a reason you can name, such as a typeface that runs small, a narrow measure or a dense professional tool.

UI text can go smaller. Start inputs and menus at `14pt` and captions at `13pt`, and rarely go below `12pt`.

## Language and direction

Mark the language of content so the system picks the right quotes, hyphenation and pronunciation. Set direction for the interface and wherever it changes inside content. Isolate a mixed-direction value such as a name, number or URL, and never reorder digits by hand. How long paragraphs and numbers behave is in [wrapping-and-punctuation.md](typography/wrapping-and-punctuation.md#internationalization).

## Trim text boxes in tight containers

In buttons and badges, the space a font reserves above and below its letters makes text sit low. Center on the cap height and baseline, not the line box.

## Decorative text stays text

Build drop caps, gradient text, outlines and text shadows as styled live text, not images, so the text stays selectable, searchable and scalable.

## Keep useful text selectable

Let people select and copy text they may reuse: long-form content, IDs, codes, addresses and error messages. Selection styling can carry brand, as long as the selected combination stays legible.

Disable selection only on a draggable or gesture-driven surface where accidental selection interferes. Never across the interface and never because a button label can be highlighted.

## On the web

- Use CSS properties over raw tags: `font-weight: 650`, not `font-variation-settings: "wght" 650`; `font-variant-numeric: tabular-nums`, not `font-feature-settings: "tnum" 1`. Leave `font-optical-sizing: auto`. [variable-fonts-and-opentype.md](typography/variable-fonts-and-opentype.md#disable-synthesis-narrowly) shows narrow synthesis control.
- Wrapping: `text-wrap: balance` (Chromium ignores it past six lines), `text-wrap: pretty`, `overflow-wrap: break-word` (`anywhere` inside a flex or grid row, the only value that also lets the box shrink), `white-space: nowrap`, `text-align: start`.
- Truncation: `overflow: hidden`, `text-overflow: ellipsis` and `white-space: nowrap` for one line; `display: -webkit-box`, `-webkit-box-orient: vertical`, `-webkit-line-clamp` and `overflow: hidden` for several.
- Case with `text-transform`; underlines with `text-underline-position: from-font` and `text-decoration-thickness: from-font`.
- Language and direction with `lang`, `dir` and `<bdi>`.
- iOS Safari zooms the whole page when an input's text is smaller than `16px`. Either size the input up on mobile, which changes how it looks on small screens, or keep `font-size: 16px` and scale it to the intended size, which is identical at every viewport but more code. Choose the one the design needs and name the other.
- Apply `-webkit-font-smoothing: antialiased` and `-moz-osx-font-smoothing: grayscale` once on the root, never per component.
- `text-box: trim-both cap alphabetic` trims text boxes as a progressive enhancement ([support](typography/spacing-and-sizing.md#text-trimming-with-text-box)).
- `::selection` for selection styling.
- The files in [typography/](typography/) are web recipes.

| Web pattern | Fix |
| --- | --- |
| `font-weight` value with no matching weight in the loaded `@font-face` files | Load that face or use a weight the family ships |
| `font-synthesis: none` on body or interface text | Remove it; set only the unwanted longhand after checking the fallback stack |
| `font-variation-settings: "wght"` or `"opsz"` | `font-weight`; drop `"opsz"` so `font-optical-sizing: auto` applies |
| `font-feature-settings: "tnum"` or `"zero"` | `font-variant-numeric: tabular-nums` or `slashed-zero` |
| `line-height` in `px` or `rem` | A unitless value |
| `leading-none` or `leading-tight` on a description, card body or anything that can wrap | `1.4` or more |
| `letter-spacing` in `px` | The same value in `em` |
| Body `font-size` in `px` | `rem` |
| Weight `100`–`300` or `font-thin`, `font-light` on text under `18px` | `400` or heavier |
| `text-wrap: balance` on a paragraph | `text-wrap: pretty` |
| `text-align: justify` in application UI | `text-align: start` |
| `-webkit-line-clamp` without `display: -webkit-box` | Add `display: -webkit-box` and `-webkit-box-orient: vertical` |
| A timer, counter, price or numeric column without `tabular-nums` | `font-variant-numeric: tabular-nums` |
| `...`, `--` or a hyphenated range in rendered strings | `…`, an em dash or an en dash |
| `text-decoration-skip-ink: none` | Remove it; set `text-underline-offset` or `from-font` instead |
| `<input>` with `text-sm` or `14px` and no mobile override | One of the input-zoom fixes above |
| `-webkit-font-smoothing` or `antialiased` inside a component | Move it to the root |
| Mixed-direction value such as a name, number or URL without `<bdi>` or `dir` | Wrap it in `<bdi>` |
| `user-select: none` or `select-none` on a layout root or text container | Remove it; keep it only on a drag or gesture surface |

Adapted from Jakub Krehel's public better-typography (jakubkrehel/skills, commit 60bf140);
the files in [typography/](typography/) are copied unchanged.
The truncate, wrap or clamp choice is from Emil Kowalski's public
break-ui (emilkowalski/skills, commit c8a7962) ([license](../../../references/emil-kowalski-LICENSE.txt)).
See [license](../../../references/jakub-krehel-LICENSE.txt).
