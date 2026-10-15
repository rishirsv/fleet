# Workflow guidance

Read the full selected workflow when doing that job. Its templates and domain
guidance are available through the four active skills; reference files are not
separately loaded skills and do not install connector configurations.

| Job | Full reference | Skill |
|---|---|---|
| Critique | [design-critique](critique.md) | design-review |
| System audit/document/extend | [design-system](design-system.md) | design-context |
| UX copy | [ux-copy](ux-copy.md) | design for writing; design-review for critique |
| Accessibility | [accessibility-review](accessibility.md) | design-review |
| Study planning | [user-research](research-planning.md) | design-research |
| Synthesis | [research-synthesis](research-synthesis.md) | design-research |
| Developer specification | [design-handoff](handoff.md) | design |

## Evidence, tools and output

Workflow targets and arguments mean the user's current target and instructions.
Connector categories refer to actually available tools. Discover access when
needed; a listed connector is not proof of an active connection. Existing user
authorization controls external writes, publishing and messages. A reference's
suggestion to publish a wiki or create tickets does not authorize those actions.

Apply the maintained skill's scope and evidence contract when a workflow
requires facts or capabilities. Never fill a template with invented measurements,
quotes, scores, prevalence or unavailable states. Omit unsupported fields or
mark unknown. Numerical scores need an explicit rubric; research sample sizes
are planning examples, not universal rules. WCAG criteria require checking the
applicable standard and actual behavior; a screenshot does not certify compliance.
Use the user's output format when specified. Otherwise preserve the selected
workflow's Output structure (Deliverables for research planning) and substantive fields: critique strengths,
copy alternatives/localization notes, and accessibility contrast, keyboard and
screen-reader coverage. Mark unsupported fields unknown instead of inventing
values or silently dropping the dimension. No extra approval is needed for already-authorized local work.

## Design-system artifact runtime

The complete [artifact instructions](../design-system/GUIDE.md)
and runtime implement a hosted artifact contract; they are not a standalone
local editor. For local file preparation, follow [Local setup](../design-system/local-setup.md). Use them only when the user requests that artifact
format and its compatible tools are actually available. Otherwise deliver the
system's tokens, component/state documentation and previews in the project's
existing format. Do not claim to publish or emulate the proprietary runtime.

## Accessibility interpretation

WCAG 2.1 target size 2.5.5 is an advisory when auditing AA. [W3C defines 2.5.5 as Level AAA](https://www.w3.org/WAI/WCAG21/Understanding/target-size.html).
Report its 44-by-44 CSS-pixel recommendation as AAA/advisory when auditing AA,
including its exceptions. Check the requested standard/version before assigning
conformance failures. Report the actual automated tool's scope and gaps rather than assuming a fixed
percentage of coverage.

Hosted saving, collaboration and migration require compatible host capabilities;
do not claim those capabilities are supplied by local file preparation.
