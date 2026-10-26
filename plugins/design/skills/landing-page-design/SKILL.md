---
name: landing-page-design
description: "Build or refine conversion-focused landing pages and marketing campaigns: offer, audience, page structure, conversion copy, proof, and SEO. Use for landing-page work, not general app UI, dashboards, components, or interface reviews."
---

# Landing Page Design

A landing page is not a homepage. A homepage serves multiple intents. A landing page wins one intent:

**one offer → one audience → one primary action.**

This skill has two halves. **Part A** decides what the page says and how it is structured. **Part B** applies Design’s shared craft guidance to that strategy.

## Scope

Use for conversion-focused landing pages and marketing campaigns. Use `$design`
for general interface work and `$design-review` for an audit without edits.
For an existing landing page, preserve its established identity and change only
what the requested outcome needs.

Read the [context contract](../../references/context-contract.md), relevant
product sources, and the [craft floor](../../references/craft-floor.md) before
choosing a direction. Explicit user choices and an accepted reference or
incumbent design system take precedence as described in the craft floor.

Use the page strategy below to decide the content. Use Design’s shared craft
references for visual choices; this skill does not impose a separate font,
color, spacing, or motion system.

---

# PART A — Strategy and structure

## A1. Intake

Gather these before designing or writing. Ask only for what is missing, and ask in one batch rather than one question at a time.

**Purpose**
- What is the ONE primary action? (trial, demo, buy, waitlist, download)
- What is the offer, exactly what do they get?
- What counts as a conversion? (click, signup, purchase)

**Audience and context**
- Who is the ICP?
- What problem are they trying to solve?
- Top three objections, meaning why they do not convert today
- Traffic source: ads, search, social, email
- What do visitors already know when they land?

**Proof and assets**
- Proof points: logos, testimonials, numbers, case studies
- Screenshots, demo video, product GIFs
- Guarantees, refund terms, cancellation terms

**Constraints**
- Brand voice: casual or professional
- Design direction: minimal editorial, playful 3D, glass UI
- Mobile priority?

If the user cannot answer, make a reasonable assumption, state it in one line, and continue. Do not stall the build.

## A2. Page structure

**Above the fold**
1. Headline, outcome plus audience
2. Subheadline, clarifies how and adds specificity
3. Primary CTA, clear verb plus what they get
4. One proof signal, logo strip, stat, or short testimonial
5. Hero visual, product screenshot or video, or a strong illustration

**Mid page (the argument)**
6. Problem to solution, one section
7. Benefits, three to five, outcome driven
8. How it works, three steps
9. Social proof, testimonials or a case study

**Bottom (objection handling)**
10. FAQ, six to twelve questions
11. Risk reversal, trial, cancel anytime, guarantee
12. Final CTA, identical to the top

Use these sections as a starting point. Include only what helps this offer and audience decide; a short campaign need not become a twelve-section page. Use actual proof and available terms. Do not invent endorsements, metrics, guarantees, or free offers.

## A3. Layout selection

Pick one and say why.

| Type | Use when |
|---|---|
| **A. Classic hero plus sections** | The product is understandable from a hero screenshot. Most common. |
| **B. Long form story** | You need to educate and overcome skepticism. |
| **C. Minimal conversion page** | High intent traffic (email to known users), or a short offer like a download or waitlist. |
| **D. Comparison page** | Search intent includes alternatives ("X vs Y", "best for"). Usually paired with SEO pages. |

## A4. Conversion rules

**Match message to source.** If traffic comes from ads, mirror the ad headline in the hero and keep the same promise and visual tone.

**Make the next step obvious.** One primary CTA. Never place competing CTAs above the fold.

**Write benefit first.** Features are what it does. Benefits are what that means for them.

**Be specific.**
- ❌ "Save time and streamline"
- ✅ "Cut your weekly reporting from 4 hours to 15 minutes"

**Reduce risk.** Explain available terms such as a free trial, cancellation policy, or guarantee when the product actually offers them.

**Treat objections as a section, not a footnote.** Move the FAQ earlier for high friction offers. Put proof directly beside the claim it supports.

## A5. Copywriting

**Headline formulas**
- "{Outcome} without {pain}"
- "The {category} for {audience}"
- "Ship {result} in {time}"

**Subheadline.** One or two sentences. Clarify what it is and who it is for.

**CTA.** Verb plus what they get. Never "Learn more" or "Submit". Use "Start free trial", "Book a demo", "Get the checklist".

**Benefit bullets.** Bold benefit, then the proof or detail. Example: **Faster iteration** — generate three layout variants in one click.

Follow the [UX-copy guide](../../references/ux-copy.md) and inspect wrapping with the actual copy and viewport.

## A6. Build order

Work section by section, in this order:

1. Hero
2. Benefits
3. How it works
4. Proof
5. FAQ
6. Final CTA

Never rebuild the whole page on each iteration. Section by section keeps control and keeps diffs reviewable.

## A7. SEO and AEO

**Do not index** ad only campaign pages or highly time bound offers. Use `noindex` or keep them behind a non indexed path.

**Do index** evergreen offers and pages where search intent matches the promise. Add a clear title and meta description, internal links from the homepage and feature pages, and the FAQ in plain question and answer form for AEO. Add FAQ schema if appropriate.

## A8. Pitfalls

- Too many CTAs above the fold
- Vague value prop: "streamline", "optimize"
- A large feature list with no outcomes
- Proof buried at the bottom
- Mobile layout that breaks readability
- No clear next step

---

# PART B — Visual system

Build within the product’s identity. For a new page, choose a distinctive
visual direction from its subject and carry it through consistently. Use a
small set of role-based values rather than importing a fixed aesthetic.

| Decision | Read |
|---|---|
| Page composition, spacing, grouping, responsive layout | [Layout](../design/references/layout.md) |
| Font families, weights, sizes, line height, wrapping | [Typography](../design/references/typography.md) |
| Palette, surfaces, contrast, gradients | [Color](../design/references/color.md) |
| Buttons, navigation, forms, feedback, labels | [Interaction](../design/references/interaction.md) |
| Icon family, weight, size, states | [Icons](../design/references/icons.md) |
| Timing, choreography, interruption, reduced motion | [Motion](../design/references/motion.md) |

Do not require gradient headings, glass navigation, a fixed hero width, a
font whitelist, Tailwind scale snapping, or a tagline reveal. Keep content
visible before motion; avoid identical fade-up entrances on every section.
Use `$design-to-motion` when the requested outcome includes an animated product
visual or showcase. Routine navigation and control feedback follow the shared
motion guidance above.

## Content and states

Write real draft copy in the product’s voice. Use supplied proof for commercial
claims; label synthetic demonstration content honestly. Keep headings and
buttons in sentence case, and make system messages calm and specific.

Implement relevant hover, active, focus, loading, empty, and error states using
the product’s interaction patterns. Keep visible keyboard focus, accessible
contrast, reduced motion, semantic HTML, and meaningful image alternatives.
No dead links or placeholder actions presented as functional.

## Finish and verify

Check the affected layout at narrow and wide widths, real and extreme copy,
keyboard navigation, forms, and reduced motion. Include metadata, favicon,
social previews, legal links, and error routes where the page’s delivery scope
requires them; use existing destinations and content rather than inventing
legal terms or expanding a page edit into unrelated site work.

Follow [visual proof](../../references/evidence.md) for rendered claims and
[finish review](../../references/finish-review.md) before delivering implemented
UI. Explain the result with [reporting guidance](../../references/reporting.md).

---

# Output format

Before building a new page, briefly state the proposed outline, hero copy,
primary action, available proof, and visual direction. Include benefit copy,
process steps, FAQ, and an indexing recommendation when relevant to the offer.
Do not require a separate approval gate when the brief is sufficiently clear.

Then build section by section per A6. Report the visible result, verification,
and any unresolved content or behavior.

---

# Quick checklist

- [ ] One offer, one audience, one primary action
- [ ] Copy matches the traffic source and uses supported claims
- [ ] Proof and available risk-reducing terms sit near the relevant decision
- [ ] Sections suit the offer rather than a mandatory page template
- [ ] Typography, colors, spacing, icons, and motion follow the product’s system
- [ ] Craft floor, accessible states, and responsive layout checked
- [ ] Relevant links, forms, metadata, and delivery requirements work
- [ ] Rendered evidence and finish review completed for implemented UI
