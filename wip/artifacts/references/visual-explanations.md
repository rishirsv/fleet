# Visual explanations

Read this when the user wants a visual answer, a diagram would make an
explanation substantially easier to follow, or the result is an HTML page. The
skill handling the subject still owns the investigation and claims. This
reference chooses their visual form and owns the rule that HTML pages explain
visually by default.

## Choose the smallest form

Start with the least elaborate form that reveals the important relationship:

| Form | Use for |
|---|---|
| Pseudocode | Logic or an algorithm |
| Call tree | Runtime control flow |
| Component tree | UI structure; include only the state and module boundaries that matter |
| Shallow file tree | Responsibility or architectural placement |
| Mermaid | Interaction, control flow, or data flow where direction and handoffs carry the meaning |

A call tree, for example, shows control flow in a few lines:

```text
completeCheckout
  priceOrder
  authorizePayment
    recordAttempt
    callProvider
  issueReceipt
```

## Show changes in their existing shape

Use a diff when the point is what changes and the surrounding shape already
exists. Match the diff to the subject: component tree, file layout, call tree,
state transition, or control flow.

```diff
 authorizePayment
   recordAttempt
+  applyIdempotencyKey
   callProvider
```

Show the whole block when most of it is new, omitted context would hide
ownership or order, or the reader needs a copyable target shape.

## Choose HTML when the answer needs a page

Use one focused HTML artifact for a visual UI, spatial layout, dense state
comparison, or explanation that needs to be durable or shareable. Load the
`html` skill with the finished content, evidence, and reading order so it can
render the page without redoing the investigation. Follow
[Visual proof](visual-proof.md) when the result must be verified as rendered
output.

## Explain visually by default in HTML

When the user requests HTML or a skill routes to `html`, explain substantive
material visually by default. Ordinary chat answers can use the inline forms
above without creating an artifact, and omit a visual when prose is clearer.

- Before drafting, identify the relationships the reader needs: flow,
  structure, state change, dependency, ownership, comparison, or quantity.
  Choose the opening view and any additional views that each explain a
  different part of the answer.
- Start a plan with a visual overview of its phases, dependencies, decisions,
  or owners. Keep the full steps, owners, constraints, and verification after
  it; the overview does not replace them.
- In an explainer, show the important flow, structure, state change, or
  comparison before the detailed explanation. In a report, visualize the
  relationships or quantitative findings that help the reader assess its
  claims.
- Draw only supplied facts. Do not invent dependencies, numbers, or
  recommendations to fill a figure. When the material has no useful
  relationship to draw, use the form that explains it clearly.
- When the user, a calling skill, or a template fixes the reading order or
  regions, place visuals in the first location that order permits and follow
  any explicit format constraint.

## Keep visuals tied to evidence

Keep each visual beside the short text it supports. Use real labels and facts
from the owning skill's evidence. Include only the calls, files, props, states,
and boundaries needed to answer the question. Use several views when they
teach different parts of the answer, but do not turn the available forms into
a checklist. Omit a figure that would only repeat a sentence; keep a useful
one even when prose could also describe the relationship.
