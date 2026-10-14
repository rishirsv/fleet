# Duplicate ownership

Use this when the same rule, contract, default, validation, transformation, or
state appears to have more than one owner.

## Classify before changing

Define the audit target by feature, contract, package, or file set.

- **Duplicate policy:** the same business or product rule is owned in more than
  one layer.
- **Local duplication:** nearby code repeats one stable operation.
- **Boundary adapter:** one component translates vendor data, network messages,
  stored data, or untrusted input at the point where it enters the system.
- **Domain constraint:** security, path, runtime math, or presentation logic is
  correctly local to its domain.

Search for repeated behavior even when names differ. Look for duplicate
validation or defaults, code that repairs trusted state at runtime, and
conversions between stored and in-memory data. Check whether query or cache
code repeats a rule another component already enforces. Inspect wrappers that
hide a second implementation, copied serializers, and repeated construction
of hash inputs.

## Choose the responsible component

For each real duplicate, name:

1. severity and classification;
2. the exact rule and why this is duplication rather than a valid boundary;
3. every current owner;
4. the component that should retain the rule;
5. the paths to delete; and
6. any boundary adapter that genuinely remains.

Prefer the owner that gives callers a small interface, concentrates behavior
and verification in one place, and matches the repository's architecture.
Apply the
[deletion test](../skills/architecture-review/references/architecture-language.md#principles).
Keep translation at a real external, persisted, or untrusted boundary even when
only one adapter exists.

Remove the competing owners and their tests as a
[hard cut](hard-cut-policy.md); tests exercise the retained interface.

If the canonical owner cannot be established from the requested scope, report
the competing evidence and route the broader decision to Architecture Review.
