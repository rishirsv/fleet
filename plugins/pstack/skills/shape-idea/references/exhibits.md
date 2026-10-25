# Exhibits

Use an exhibit when the user cannot reasonably answer a question from prose.
Choose the smallest representation that lets them judge the consequential
difference:

- **Appearance:** show labeled alternatives in context. For a border color,
  show the same component on the same background with only the border changed;
  color names or hex values alone do not let the user judge.
- **Structure:** show a small architecture, data-flow, or state diagram when
  relationships are hard to follow in prose.
- **Behavior:** provide a tiny interactive example when clicking, timing, or
  transitions determine the answer. Use a static comparison when it suffices.

Keep the question, exhibit, and recommendation together, with matching option
labels so the user can answer "B, but subtler."

Confirm the exhibit renders in the available surface before asking for a
judgment. If it cannot be shown, explain the limitation and either defer the
visual choice or ask about the intended effect. An answer about an unseen
design is not approval of it.

Keep preparation proportional to the question. Reuse existing artifacts and
rendering tools, build only for the current frontier, and vary only what the
question tests. Use inline text, tables, or diagrams where they suffice, and
load visual tooling only when needed. Keep artifact source outside the
conversation; retain the choice, reason, and artifact link instead of repeating
previews. Leave incidental styling to later design work unless it changes the
direction or the user wants to settle it now.
