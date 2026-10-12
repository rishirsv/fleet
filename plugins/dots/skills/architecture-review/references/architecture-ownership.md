# Architecture ownership

Identify the module that should remain responsible for the rule. The layer where
a bug appears may have a different responsibility.

## Required discovery

Before deciding ownership:

- Read the repo docs that define architecture, boundaries, or responsibilities.
- Read ADRs or design docs that define runtime flow, request flow, or package boundaries.
- Inspect the top-level project structure to map the repo's concrete module or package names onto the generic layers in this reference.

When docs are incomplete:

- infer the current layer model from the codebase
- state the assumption explicitly
- keep the recommendation aligned to one canonical owner

## Required output

When answering an ownership or placement question, name the single correct
long-term owner. Explicitly separate:

- `Current owner`
- `Canonical owner`
- `Competing owners that are wrong`
- `Cleanup direction`

Do not recommend a temporary first owner. If the current owner is wrong, the
recommendation is the canonical owner and the cleanup path to get there.

## Decision order

1. Identify the runtime concern:
   - visible UI state
   - platform shell or OS bridge
   - runtime composition or request dispatch
   - canonical domain or application workflow
   - pure shared logic
   - concrete adapter or integration behavior
2. Name the layer where the wrong behavior currently happens.
3. Decide the single canonical owner for the behavior.
4. If the behavior is reusable product or business policy, move ownership out of the runtime orchestration layer.
5. Once the canonical owner is clear, remove duplicate policy, fallback logic,
   and competing paths. Keep compatibility only where persisted data or an
   external contract requires it.

## Layer map

- `UI layer`
  - owns visible UI state, navigation, rendering, presentation-oriented derived
    state, and view composition
- `Platform shell`
  - owns native shell concerns, OS bridges, local device integrations,
    filesystem or permission bridges, process or session setup and
    communication, and platform-local persistence helpers
- `Runtime orchestration layer`
  - owns runtime composition, request dispatch, background coordination, worker
    management, event publication, and process-level orchestration
  - this is not automatically the `Canonical owner`
- `Domain or application layer`
  - owns canonical product workflow, business rules, reusable application
    services, and cross-interface behavior
- `Shared core layer`
  - owns shared types, enums, validation, normalization, capability logic, and
    pure logic used across runtimes
- `Adapter or integration layer`
  - owns concrete protocol, provider, vendor, transport, or API integration
    behavior
  - does not own cross-provider or cross-integration product policy

Translate these generic layers into the repo's actual module, package, crate, or service names before making a recommendation.

## Placement rules

Each rule keeps a concern where every interface that needs it can reach one copy.

- Move reusable domain policy out of the runtime orchestration layer, even when
  the wrong behavior currently happens there; other runtimes need the same policy.
- Keep UI state, layout state, restore state, and user-facing presentation in the
  UI layer, which owns what the user sees.
- Keep platform shell and native integration concerns in the platform shell, so
  the domain or application layer stays portable.
- Put cross-provider or cross-vendor product policy in the domain or application
  layer; an adapter sees only its own provider.
- Put pure validation, normalization, and capability logic in shared core or a
  narrow domain module, where every runtime can reuse it.

## Common judgments

- If the question is "who should decide this for all future interfaces?" the answer is usually the domain or application layer, a narrow domain package, or shared core, not the runtime orchestration layer.
- If the question is "where should this behavior live after the fix?" answer with the canonical owner, not the easiest patch point.
- If the question is "who owns the wire shape or payload type?" the answer is usually the shared API or core type layer, not the runtime orchestration layer.
- If the question is "who owns vendor-specific behavior?" the answer is the relevant adapter or integration layer, but only for adapter behavior, not canonical product policy.
