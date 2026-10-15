---
name: scribe
description: "Use when Drafts is selected or the user wants help developing, drafting, or revising a piece of prose."
---

# Scribe

Use Scribe as the entry point when the user selects Drafts. Identify the live
artifact and desired outcome, then load only the writing skills needed to finish
the request. A plugin call is enough; the writer does not need to name a skill.

Scribe is the only automatically discoverable Drafts skill in Codex. The focused
skills remain directly callable and available through the links below. Read the
selected skill's `SKILL.md` before applying it; resolve links relative to this
file, not the user's working directory. Do not load the whole catalog or ask the
writer to invoke each stage. If the user names a skill or editorial pass, honor
that choice before considering a broader workflow.

## Find The Writer's Starting Point

Read `../../references/context-contract.md` before substantial work. Follow its authority order, project routing, provenance, destination, and write-safety rules.

At the first meaningful Drafts interaction, inspect the request, supplied material, current workspace, and maintained context before choosing a route.

- Treat an existing writing workspace, maintained voice or style context, or useful live artifact as a real starting point even when the Drafts scaffold is absent.
- If the user brings a draft, notes, sources, an active workspace, or enough context to begin, do the immediate writing work. Do not block on setup or a calibration interview. Offer to strengthen durable context only when it would materially improve future work.
- If there is no established writing context and no useful artifact to work from, briefly explain the benefit of one writing home: it keeps how the writer sounds, what their writing needs to do, examples, and drafts together so future sessions can start with less re-explaining.
- Guide that writer through one simple setup without requiring them to know the skill catalog. Resolve the target folder first, then route to `setup-project` and begin `onboarding` for `VOICE.md` and `STYLE.md`.

Do not create files until the destination is explicit or safely resolved from the user's request. Do not present multiple homes or a project system during normal first use. Another self-contained folder remains an optional manual capability only when the user explicitly asks for it later.

Treat `TASTE.md`, `context.md`, `published/`, and `.status.yaml` as legacy or workspace-specific surfaces, not requirements.

## Route By Outcome

Choose the smallest route that fits the request:

| User state or outcome | Route |
|---|---|
| First meaningful interaction with no writing home or useful artifact | Brief orientation, resolve the target, [Setup Project](../setup-project/SKILL.md), then [Onboarding](../onboarding/SKILL.md) |
| Explicitly asks to set up or migrate a writing home, or create another self-contained writing folder | [Setup Project](../setup-project/SKILL.md), then optional [Onboarding](../onboarding/SKILL.md) |
| Wants to create, calibrate, import, or refresh voice and style guides | [Onboarding](../onboarding/SKILL.md) |
| No idea yet | [Brainstorm](../brainstorm/SKILL.md) |
| Has a live idea and needs material | [Interview](../interview/SKILL.md) |
| Needs the point sharpened | Read [Thesis](../../references/thesis.md) for thesis options |
| Needs the reader promise sharpened, or has notes that need structure | [Outline](../outline/SKILL.md) |
| Needs the most important idea or real opening found and placed | [Dev Edit](../dev-edit/SKILL.md) |
| Has notes, an outline, or partial prose and asks for a complete draft | [Draft](../draft/SKILL.md) |
| Needs argument, structure, stakes, or evidence reviewed or fixed | [Dev Edit](../dev-edit/SKILL.md) |
| Structure is stable and prose needs revision | [Line Edit](../line-edit/SKILL.md) |
| Needs a first-time-reader or fresh-eyes cold read | [Reader](../reader/SKILL.md) |
| Asks to remove AI residue or machine-smoothed patterns | [AI Check](../ai-check/SKILL.md) |
| Asks whether prose sounds like the writer or matches established voice guidance | [Voice Check](../voice-check/SKILL.md) |
| Needs publication, project, or format standards | Load the active `STYLE.md`, brief, template, or maintained workflow |
| Needs a publication-readiness decision | [Final Pass](../final-pass/SKILL.md) |
| Needs argument and reader feedback | [Dev Edit](../dev-edit/SKILL.md), then [Reader](../reader/SKILL.md) |
| Asks to save a confirmed writing preference or editorial lesson | [Save](../save/SKILL.md) |

The familiar sequence remains available:

```text
brainstorm -> interview -> outline -> draft -> dev-edit -> line-edit -> final-pass
```

Treat it as a map, not a gate. Skip resolved stages and jump backward when the material reveals a deeper problem.

## Start The Work

1. Identify the requested outcome and whether there is a useful artifact or established writing context.
2. Locate the active artifact: supplied text, named file, current draft, notes, source room, outline, or destination document.
3. Load the relevant voice, workspace, assignment, and source context.
4. Handle first-run setup only when the starting-point check shows it is needed.
5. State the route briefly when it includes several meaningful passes.
6. Begin. Ask a question only when a missing answer would materially change the work and cannot be inferred safely.

Do not lead with a tour of every feature. The user came to write, not admire the plumbing.

## Compose Skills Deliberately

- Use one skill when one skill can finish the job.
- When a selected skill calls another pass, read that skill's instructions from
  the linked folder before applying it. Keep automatic checks silent when the
  selected workflow requires it; a diagnosis-only request remains diagnosis-only.
- Put diagnosis before revision and validation after revision.
- Run `dev-edit` before line-level passes when the argument or structure is unstable.
- Apply publication, project, and format requirements from the active `STYLE.md`, brief, template, or workflow while drafting or revising.
- Keep source provenance attached throughout the workflow.
- Preserve the writer's ownership of thesis changes, major reframes, and consequential cuts.

Common compositions:

- **Lede repair:** `dev-edit` -> targeted structural revision -> optional `line-edit`
- **Muscular revision:** `dev-edit` -> revision -> `line-edit` -> `ai-check`
- **Pre-publication:** `dev-edit` when needed -> `ai-check` -> `final-pass`
- **Voice repair:** `voice-check` -> targeted revision -> `ai-check`
- **Argument and reader review:** `dev-edit` -> `reader` -> writer judgment -> targeted revision

## Artifacts And Progress

- Respect the project's existing folder and versioning conventions.
- Do not create a parallel draft workspace by default.
- In a writing home initialized by `setup-project`, create or reuse `drafts/<piece-slug>/` and keep that piece's versions, notes, research, outline, reviews, and related material there.
- In any other existing project, create or reuse one dedicated piece folder in the location its conventions require. Do not impose `drafts/` retroactively.
- Update an existing status file or tracker only when the user asked for progress tracking or the project workflow requires it.
- Name draft iterations `version one`, `version two`, and so on when a named version is needed.
- Put substantial reviewable output in the destination required by the governing workspace; otherwise keep the project-local source of truth.

## Completion

Finish the requested outcome instead of automatically pushing the user into the next stage. Then report:

- what changed or was produced;
- any source, thesis, or editorial uncertainty that still needs judgment;
- any recurring preference or failure pattern worth capturing through `save`.
