---
name: walkthrough
description: "Build scripted UI walkthroughs and staged product illustrations with StageShow. Use when a mock interface should act out an action, not for working prototypes."
---

# Walkthrough

Build an authored visual scene showing a specific product interaction: a believable interface, framed in its space, as one still or a short animation in which one thing happens. StageShow's cursor and state changes are scripted; they do not operate the real app. Say so when handing it over, and never claim that a scripted scene validates actual product behavior. For a freely interactive prototype or shipping UI, use `design`; for faithful animation of an accepted design, use `design-to-motion`. Canvas owns editable Canvas artboards.

## Ground the scene

Read the product's design guidance, actual UI, assets and tokens before choosing a look. Existing product decisions and the user's brief take precedence over kit defaults. Identify any approximations, especially native platform materials or behavior not verified against a running product. Follow the design plugin's [context contract](../../references/context-contract.md) and [craft floor](../../references/craft-floor.md). Reduced motion shows a useful final still.

## Build and rehearse

Follow the [StageShow workflow](references/workflow.md): plan the medium, look and story before code, start from the closest bundled gold example, build the screen, choreograph, then rehearse against the gold. Its references in [vendor/references/](vendor/references/) hold the framing, craft, motion, kit and rehearsal rules; read the ones the scene needs.

Copy the example and `kit/` into a working project; never write into an installed plugin cache. For a standalone experiment, copy `vendor/` to a writable working directory, run `npm ci` and `npm run dev` there, and use the playground; it requires Node 20.19 or newer. For host projects, use their existing build and dependency conventions. Use the filming tools when available, respecting host browser preflight requirements; automated checks do not replace watching. Explain what was built and what was not verified.

## Attribution

The vendored source is pinned and adapted as recorded in [NOTICE](vendor/NOTICE.md); retain its [MIT license](vendor/LICENSE) in copies containing substantial portions. Third-party app artwork and brand registries are excluded. Use only assets the user supplies or has rights to use.
