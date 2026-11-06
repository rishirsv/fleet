---
name: design-to-motion
description: "Animate an accepted static design, Figma frame, or screenshot as a faithful showcase or site section, with video or GIF export. Not for product interaction motion."
---

# Design to Motion

A showcase animation is not a redesign. The viewer must see **the exact design**, and must see that **it is alive**.

**exact frame → empty state → smooth load → every visual acts out its story → seamless repeat.**

This skill has three parts. **Part A** ([fidelity](references/fidelity.md)) rebuilds the design so the finished frame is indistinguishable from the source. **Part B** ([motion system](references/motion-system.md)) is the motion system; its **Make it yours** table holds every value. **Part C** ([export](references/export.md)) records and exports. Before delivering, run the [quick checklist](references/checklist.md). Work through A before touching B, and never encode anything before the checks in A7 and B9 pass. Parts A and B apply in both contexts below; Part C is for the showcase, or for a website only when exports are asked for.

## Scope

Apply to any request to animate a static design: Figma frames, UI cards, dashboards, app screens, marketing heroes, product mockups, and designs placed on a photo background. Preserve the user’s explicit choices, accepted design, and incumbent design system. On a website, read the [context contract](../../references/context-contract.md), [craft floor](../../references/craft-floor.md), and [product motion guidance](../design/references/motion.md). Faithful recreation of an accepted target follows the craft floor’s reference exception; showcase timing does not become a site-wide interaction rule.

For a scripted product walkthrough built as a mock UI, use `$walkthrough`. Use this skill when faithfully animating an accepted design or exporting its showcase.

**Not for** interaction motion inside a shipping product (hovers, menus, toasts). For that, use Design’s [product motion guidance](../design/references/motion.md). **Companion skill:** `$landing-page-design` for conversion strategy when the animation will live on a landing page.

## Two contexts

Decide the context before anything else. It changes what you animate, how the motion starts and ends, and what you deliver.

| | **Showcase** | **Website** |
|---|---|---|
| Typical request | "Animate this design for me", a Figma link and nothing else | Building or editing a landing page or site, or the request names one |
| What gets animated | The whole frame | Only the sections that qualify (table below) |
| Start | Page load, from the empty state | When the section scrolls into view, once |
| After the intro | Stories run, then the frame dissolves and the cycle repeats (B5) | Stories run forever. No dissolve, no cycle |
| Text | Exported layers, so the frame is pixel exact | Live HTML text in the site's font, for SEO and accessibility. Only the visual parts are exported images or SVG |
| Deliverables | The page plus MP4 for X, website GIF, 800×500 GIF (Part C) | The animated sections inside the site's code. Exports only when asked |

If the request does not say which, look at where you are working: inside a site's codebase, assume website. With only a design and no site, assume showcase. If it is still unclear, assume showcase and say so.

### Website: which sections get which motion

Scan the page section by section. Apply this skill only where a section has a visual part. Never animate a text section with it.

| Section | Apply |
|---|---|
| Bento and feature sections: cards with text plus a visual (a chart, list, flow, calendar, prompt, player) | Card intro on scroll (B2, `card` kind, text included), then a story loop on each card's visual (B4). This is the main use on a landing page |
| Product or dashboard mockup (a hero shot of the app, a product screenshot) | The loading intro on scroll: surfaces stay, contents load (A5). Stories after loading are opt-in: offer them in the report. Do not add them unasked |
| Logo rows, integrations | A marquee or a gentle light up story |
| Text only sections: headline blocks, testimonials, FAQ, pricing, CTA, footer | Not this skill. Keep the page’s established behavior; do not add a default scroll reveal |

Website rules:

- **Trigger with `IntersectionObserver`.** Start the intro when about 30% of the section is visible. Play it once. Never use a scroll listener.
- **Pause stories off screen.** Stop the clock when the section leaves the viewport and resume it on return.
- **Stagger by reading order inside the section**, never across the whole page.
- **Respect the site's system.** Use its components, tokens, radii, and fonts. Keep essential content visible and usable while optional visual layers load; provide a still fallback if scripts or motion are disabled. Provide a pause control for prolonged automatic movement as required by the shared motion guidance. Fidelity to the design still applies (A7), compared section by section.
- `prefers-reduced-motion: reduce` shows each section in its final state with no stories.

## Output format

Before building, state in a few lines:

1. **Context** — showcase or website. For a website, list each section and what it gets (intro and stories, intro only, or nothing)
2. **Layout** — app frame (which joined surfaces stay static) or separate cards (which cards rise in), and the clip shapes
3. **Background** — kept exactly, or what cannot be reproduced
4. **Choreography** — load order and the kind per element group
5. **Stories** — one sentence per visual saying what it acts out, plus any accents
6. **Cycle** — total length and phases

After building, report:

- Still frame fidelity (overall and worst surface PSNR)
- Overflow check and seam check results
- The three files with size, dimensions, frame rate, and duration
- Anything not reproduced exactly, named plainly

For website implementations, follow [visual proof](../../references/evidence.md)
and [finish review](../../references/finish-review.md). Report only the exports
requested for that context and the checks actually performed.
