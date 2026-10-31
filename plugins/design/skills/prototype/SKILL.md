---
name: prototype
description: Create scripted product UI illustrations and animated walkthroughs with StageShow's React kit. Use for a staged action and outcome in a mock interface, not for a freely interactive prototype, production UI, or faithful animation of an accepted design.
---

# Prototype

Build an authored visual scene showing a specific product interaction. StageShow's cursor and state changes are scripted; they do not operate the real app. Say so when handing it over. For a freely interactive prototype or shipping UI, use `design`; for faithful animation of an accepted design, use `design-to-motion`. Canvas owns editable Canvas artboards. A StageShow React scene is not an editable Canvas artboard or evidence that the product works.

## Ground the scene

Read the product's design guidance, actual UI, assets and tokens before choosing a look. Existing product decisions and the user's brief take precedence over kit defaults. Preserve meaningful states and actions. Identify any approximations, especially native platform materials or behavior not verified against a running product. Follow the design plugin's [context contract](../../references/context-contract.md) and [craft floor](../../references/craft-floor.md).

Choose the intended placement, size, focal object, three to five beats, and a payoff. Reuse the product's own components when appropriate. Otherwise adapt the bundled React and CSS kit. Design the narrow view as well as the wide one where relevant. Reduced motion should show a useful final still.

## Build and rehearse

The bundled [StageShow kit and examples](vendor/) come from Benji Taylor's StageShow. Its [framing](vendor/references/framing.md), [craft](vendor/references/craft.md), [motion](vendor/references/motion.md), and [kit](vendor/references/kit.md) guides explain the approach. Read only the parts relevant to the scene. Choose an example actually present in `vendor/examples/`; some upstream guides mention examples or brand assets omitted from this distribution. Copy it and `kit/` into a working project, then adapt its structure and script. Do not write into an installed plugin cache.

For a standalone experiment, copy `vendor/` to a writable working directory, run `npm ci` and `npm run dev` there, and use the playground. It requires Node 20.19 or newer. For host projects, use their existing build and dependency conventions. Name targets and measure them instead of hard-coding cursor coordinates. Set a poster state and make the action, result and reset legible.

Watch the sequence at its intended size, inspect key states and the narrow layout, and check reduced motion. Use the filming and verification tools in [rehearse](vendor/references/rehearse.md) when available, respecting host browser preflight requirements. Automated checks do not replace watching. Explain what was built and what was not verified. Never claim that a scripted scene validates actual product behavior.

## Attribution

The vendored source is pinned and adapted as recorded in [NOTICE](vendor/NOTICE.md); retain its [MIT license](vendor/LICENSE) in copies containing substantial portions. Third-party app artwork and brand registries are excluded. Use only assets the user supplies or has rights to use.
