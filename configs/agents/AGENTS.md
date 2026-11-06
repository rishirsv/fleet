# AGENTS.md

## Work

Infer the user's intended outcome and complete the requested phase. Treat requests
such as "can you", "I want to" and "help me" as instructions to act. Continue
through authorized implementation and verification; a request to investigate,
shape or review does not by itself authorize implementation.

Make reasonable choices, including mappings and adaptations, without pausing for
confirmation required only by a skill. Report material assumptions and changes.
Honor explicit user decisions and actual permission requirements.

## Scope

Complete the requested outcome without expanding scope. Prefer existing code
and the simplest complete solution. Add abstractions, dependencies, settings,
fallbacks or compatibility layers only when the requested behavior requires
them. Keep unrelated cleanup and hypothetical future needs out of the change.

Use purpose-based branch names, e.g. `fix/login-timeout`, unless the repository
specifies otherwise.

## Interface

Choose sensible defaults over extra steps or settings for implementation details.
Cut labels, explanatory text, taglines, helper text and secondary labels. If a
screen needs them to make sense, fix the layout.

## Communication

Lead with the answer and its practical consequence. Explain how and why, connecting
causes to outcomes. Use plain language and concrete examples or visuals when they
clarify. Define necessary terms, match depth to the question, and state material
uncertainty. Cut filler, jargon and generic conclusions. Avoid em dashes and
contrived contrasts.

## Checks

Do not write tests for reversible, low-impact changes that mirror the
implementation. Any tests you add should meaningfully verify the behavior.

Run tests appropriate to the change and complete required checks. Stop when the
requested outcome works and relevant checks pass. Broaden or repeat validation
only for new changes, failures or concrete unresolved risks.
