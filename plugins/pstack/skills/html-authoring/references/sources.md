# Source notes

Research record for this scaffold, 26 October 2026. This is not a runtime
reading requirement. The skill must remain usable without fetching sources.

## Thariq Shihipar

- [Article](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html): the five use-case headings in SKILL.md are retained directly. The scaffold covers comparisons, visual explanation, portable references, and editor exports.
- [Companion examples](https://github.com/ThariqS/html-effectiveness), revision `1787245d94aa680edf18b52027e3f859032776ba`: standalone documents with no build step. Inspected the gallery inventory and the triage/feature-flag export implementations. No example code is copied into this skill.

## Official Anthropic skills

Read from [anthropics/skills](https://github.com/anthropics/skills), revision
`dbd4588f9e1033efb41dad4bef2f7947c8993d44`:

- `skills/web-artifacts-builder/SKILL.md`: separates elaborate multi-component artifacts from simple single-file work; bundles dependencies for delivery. Its prescribed React stack and optional-test sequencing are not requirements here.
- `skills/frontend-design/SKILL.md`: subject-specific composition, existing-brief precedence, typography, restrained motion, accessible interaction, and purposeful copy. Detailed design guidance stays with Design rather than being duplicated here.
- `skills/webapp-testing/SKILL.md`: inspect the rendered result and exercise the requested behavior. Use the current environment's browser tools, not its prescribed Python Playwright launcher.

## Confirmed reference repository

The user confirmed [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks).
Read at revision `b7f286c71d043ad788be772a881179a07c178513`.
The repository declares CC0. These are unofficial extracted prompts, not an
authenticated description of APIs available in this environment.

### Full skill reads and ownership

Every SKILL.md listed below was read in full. Paths are relative to `Anthropic/`.
Retained portable passages use the source wording; no independent copy of the
same guidance is kept in multiple references.

| Source | Destination / decision |
|---|---|
| `claude-code/skills/artifact-design/SKILL.md` | Entrypoint structure and process; `design.md` owns fundamentals and editorial treatment. Title belongs only to the entrypoint. |
| `claude-code/skills/artifact-diagramming/SKILL.md` | `diagrams.md`: mechanism-first diagrams and inline SVG mechanics. |
| `claude-code/skills/artifact-capabilities/SKILL.md` | `interactions.md`: state ownership and runtime boundary. Claude API declarations and contracts do not transfer. |
| `claude-design/skills/make-a-doc/SKILL.md` | `documents.md`: flowing pages versus fixed sheet, pagination and typography. |
| `claude-design/skills/save-as-pdf/SKILL.md` | `documents.md`: fresh print copy, relative paths, selectable output and delivery. |
| `claude-design/skills/save-as-standalone-html/SKILL.md` | `standalone-html.md`: copy, discover code-referenced assets, inline, bundle, verify, deliver. |
| `claude-design/skills/interactive-prototype/SKILL.md` | `interactions.md`: working state and transitions. |
| `claude-design/skills/make-tweakable/SKILL.md` | `interactions.md`: small controls for high-impact values. |
| `claude-design/skills/options/SKILL.md` | `interactions.md`: anchored rounds and stable option IDs. |
| `claude-design/skills/html-email/SKILL.md` | `email.md`: email-specific markup, layout and client constraints. |
| `claude-design/skills/frontend-design/SKILL.md` | Read; artifact-design owns overlapping visual guidance. No second conflicting aesthetics checklist. |
| `claude-design/skills/hi-fi-design/SKILL.md` | Read; its options instructions duplicate `options`. Product design process stays with Design. |
| `claude-design/skills/wireframe/SKILL.md` | Read; same options duplication. No mandatory interview or variation count added to HTML authoring. |
| `claude-design/skills/handoff-to-claude-code/SKILL.md` | Read; distinguishes HTML design references from target-app production code. Full developer-handoff packaging stays with Design. |
| `claude-design/skills/claude-api-in-prototypes/SKILL.md` | Read; no equivalent injected API assumed. Runtime boundary in `interactions.md`. |
| `claude-design/skills/flier/SKILL.md` | Read; fixed-sheet behavior belongs to `documents.md`; no separate flier workflow in this scaffold. |
| `claude-design/skills/maps-geography/SKILL.md` | Read; specialized cartography remains outside this scaffold, rather than silently adding map dependencies. |

Scope: HTML authoring and its direct composition, interaction and export modes.
Slide decks, video, 3D, hosted artifact types and their service implementations
remain separate workflows; this is not a claim to have audited that repository
in full.

### Adaptations

- Complete HTML documents replace Claude's injected skeleton, `<helmet>`, and
  canvas-mode metadata. Ordinary responsive layout replaces host pan/zoom.
- Available browser tools replace `show_html`, `ArtifactCheck`, and webview
  logs; actual file links replace `present_fs_item_for_download`.
- Existing bundling tools or direct inlining replace `super_inline_html`.
  Its private resource registry and required thumbnail are not portable.
- Print CSS or an existing project component replaces `doc-page`,
  `show_pdf_export_dialog`, and private provenance metadata.
- Destination-specific API discovery replaces `window.claude`, capability
  declarations, shared storage, self-publishing and automatic hot reload.
- Offline packaging replaces mandatory CDN loading; host-specific allowlists,
  size limits and font restrictions are not asserted for local files.
- Native page controls replace an injected Tweaks panel; React is used when
  the project or behavior needs it, not as a required dependency.
- The upstream single-check ceiling conflicts with Fleet's instruction to
  recheck concrete defects; proportional verification replaces that ceiling.
- Email delivery uses actual footer details and truthful client-test status,
  rather than invented addresses or an unverified send-ready claim.

The last two are explicit correctness/instruction adaptations, not tooling
renames. All other unselected source workflows are scoped out rather than
silently rewritten into generic advice.

## Earlier Fleet skill

Reviewed `plugins/dots/skills/html/SKILL.md` at `72a2cc6^`.
Preserve its document/page-set/embed distinction, plans, PR walkthroughs,
charts, diagrams, interaction, and precise delivery status. Its custom helpers,
visual style, and capture runner remain outside this initial scaffold pending
review; they have not been reintroduced or declared obsolete.
