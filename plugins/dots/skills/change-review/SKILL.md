---
name: change-review
description: "Reviews a diff, branch, or pull request for defects and maintainability, with configurable independent reviewers. Repairs supported findings unless the user requests review-only."
---

# Change review

Review a completed change against its intended behavior and repository
constraints, then repair supported findings as described in
[Repair before reporting](#repair-before-reporting).

## Fix the review target

- Use the target named by the user. Otherwise review the current branch and its
  staged, unstaged, and untracked changes.
- If the selected target has no changes, report that there is no reviewable
  diff and stop before spawning a reviewer.
- For a pull request, use its actual base and head.
- For a base-branch review, compare what would actually merge. Use the base
  branch's configured upstream when it exists and is ahead of the local base;
  otherwise use the local base. Run `git merge-base HEAD <comparison-ref>`, then
  inspect `git diff <merge-base-sha>`. If the local base cannot be resolved, try
  its remote-tracking ref before reporting the target unavailable.
- Recover the intended behavior from the request, pull-request description,
  linked issue or specification, commits, and code.
- Keep the target fixed during review. Restart if it changes unexpectedly. Ask
  only when ambiguity would materially change what success means.

## Choose the level

The user can pass a level, a mode, and a target in any order, for example
`$change-review high`, `$change-review medium review-only`, or
`$change-review max #123`. The level sets how many independent reviewers run;
`low` is the default. These are review-depth presets, not model reasoning-effort
settings. `$change-review` and `$change-review low` both launch exactly one
fresh subagent; do not add agents for discovery, summarization, or verification.

| Level | Reviewers | Assignment |
|---|---|---|
| `low` | 1 | the whole change |
| `medium` | 2 | split by changed paths, or correctness and design when the diff is small |
| `high` | 3 | correctness; design and simplicity; tests, security, and performance |
| `xhigh` | 4 | `high`, plus what the change can break outside the diff |
| `max` | 5 | `xhigh`, plus one reviewer on a different model through `$ask-model` when one is available |

A positive count overrides the table, for example `$change-review 2`. `review-only`
reports findings without editing files.

## Coordinate review

Use this section only when coordinating the review. A delegated reviewer skips
it and follows **Review the assigned change** directly.

When the user requests an external reviewer such as ChatGPT Pro, prepare the
fixed target, intended behavior, and review-only instructions for a manual
handoff. Do not substitute another model or claim the review ran until its
complete result is returned. Repository access and model selection belong to
the external chat; Dots does not provide or configure that connection.
Otherwise use the local reviewer workflow below.

1. Review through independent reviewers, even for a narrow diff, because the
   implementer tends to share the assumptions that produced a defect.
2. Spawn each reviewer fresh and read-only, with an adversarial stance. Use an
   adversary or reviewer role when one is available; otherwise use a fresh
   subagent and have it load this skill. An agent that implemented
   any part of the change must not serve as its independent reviewer.
3. Give the reviewer the fixed target, intended behavior, any review focus the
   user requested, applicable repository instructions (including ancestor and
   changed-directory instructions), and changed paths. Use the smallest
   sufficient context without inherited conversation history. Let
   the reviewer inspect the changes directly rather than sending the
   implementer's reasoning or conclusions.
4. Use the number of reviewers the level sets. Do not increase it automatically
   or pause a default review to propose a higher level. Allocate the available
   reviewers to the most consequential risks in this target.
5. When using several reviewers, give each a distinct assignment from the
   level table. When splitting by paths, assign each changed path to one
   primary reviewer. Add a review assignment for interactions only when those
   interactions need separate review. A reviewer may inspect outside its
   assigned paths for context but reports findings only for its assigned paths.
   Do not give every reviewer the same undivided diff.
   At `high`, `xhigh`, or `max`, request an
   [omissions sweep](#optional-omissions-sweep) in the initial briefs when a
   large diff, moved logic, or changed lifecycle or configuration makes gaps
   likely. Each assigned reviewer does it within its existing assignment and
   context before returning findings; it adds no reviewers or verification
   agents and does not reserve a reviewer solely for the sweep.
6. Wait for every reviewer to finish; each returns all findings for its
   assignment in one response. Then merge duplicates and combine related
   findings while preserving the evidence required for each finding. Resolve
   material disagreement only when needed; do not repeat each reviewer's
   investigation. The reviewer owns verification of its findings. Do not launch
   per-finding validation agents or a second consensus pass. Resolve a material uncertainty
   with the smallest targeted check, reusing the assigned reviewer if needed.
7. Repair or report the combined findings as described in
   [Repair before reporting](#repair-before-reporting).

If no fresh reviewer is available, review the complete change yourself and
label the result `Independent review unavailable.` Do not describe your own
review as independent.

## Review the assigned change

A delegated reviewer inspects the assigned target directly and returns its
findings to the coordinating agent. It does not spawn or delegate another
reviewer, edit files, create commits, push branches, or post review comments.

Inspect the complete diff for the selected target or assigned portion and enough
surrounding code, call sites, and tests to understand each changed path.
Continue through the whole diff after finding an issue. Verify every candidate
against the available code, callers, tests, results, and repository rules before
returning it.

### Correctness

- Compare the implementation with the task or specification and the
  repository's review guidance.
- Check contracts, happy and failure paths, null and empty inputs, boundary
  values, state transitions, errors, cancellation, and removed safeguards.
- For deleted or replaced logic, identify the invariant it enforced and where
  the new implementation preserves it.
- Trace affected callers and callees. Demonstrate the reachable path for any
  problem that depends on a value or state.
- Probe for off-by-one errors, inconsistent state, repeat execution, partial
  failure, and race conditions when relevant.
- Check the changed language and framework's failure modes, such as coercion
  or truthiness, captured or stale state, mutable defaults, iteration semantics,
  and time or numeric conversions. Trace a concrete trigger rather than
  reporting a generic pitfall.
- For wrappers, proxies, caches, decorators, and adapters, trace forwarded
  operations to the intended underlying instance. Look for accidental re-entry
  through a registry or global lookup, recursion, and missing forwarding for
  methods callers use.
- Check what the change can break outside the diff. Name the one fact its
  safety depends on, such as "no caller passes an empty list" or "nothing else
  reads the old field". Look for consumers a text search misses: persisted or
  serialized data, configuration, generated code, string-keyed lookups,
  scheduled jobs, and other repositories. When a read-only query or short
  script can prove that fact, run it and cite the result.

### Readability, simplicity, and ownership

- Name a simplification finding only when a concrete shorter form preserves the
  required behavior and ownership. Identify the current maintenance cost and the
  code to delete or inline, or the existing owner or platform facility that
  replaces it.
- Prefer the standard library, platform API, or canonical repository utility. Remove duplication, unused
  state, state that can be calculated from existing data, artifacts that have no
  effect, and comments that restate the code.
- Collapse repeated branches when one existing owner can express the policy. Add
  a helper or model only when it removes duplicated policy rather than renaming
  it.
- Flag new indirection or a dependency only when it has no current
  responsibility or required boundary and a concrete alternative reduces
  production concepts without weakening ownership or behavior.
- Before deleting or inlining code, identify the invariant or constraint it
  serves. Consult history only when current code, tests, and documentation do
  not explain it.
- Keep logic, policy, and validation in the layer responsible for them. Flag
  added coupling, blurred state ownership, circular dependencies, crossed module
  boundaries, or leaked implementation details when the change causes a concrete
  maintenance cost.
- Check whether a new guard, retry, fallback, or cast repairs the responsible
  contract or merely hides its failure. Keep a guard only when a named caller
  can produce the state it handles.
- Flag what an abandoned approach left behind: names and comments that
  describe the old design, identifiers or string keys renamed in one place but
  still referenced elsewhere, and warnings or checker rules suppressed to make
  the change pass.
- Judge domain modeling, boundary parsing, types, rerun safety, and shared
  writers with [Engineering principles](../../references/engineering-principles.md).
- Separate orchestration from low-level detail. Flag unnecessary serialization
  or partial updates when a clearer atomic structure is available.
- Remove obsolete dual paths as
  [Hard-cut policy](../../references/hard-cut-policy.md) directs.
- Clean up style in changed lines: names, idioms, comment density, and structure
  that diverge from the surrounding code or repository conventions, and verbose
  constructs with a shorter idiomatic form. Skip anything a configured formatter
  or linter already enforces.

### Tests

- Treat tests as durable product contracts, not as a checklist of changed code.
  Review applicable existing test results, but do not run builds or test suites
  during the review.
- Judge which tests to keep, add, move, or remove, and spot tests that look
  useful but prove nothing, with
  [Test consolidation](../../references/test-consolidation.md).
- Derive expected results independently of the implementation. Identify a
  plausible broken implementation that the assertion would reject.
- Treat rendered or manual evidence as proof of the current result, not a
  replacement for durable regression protection when automation is practical.
- For assertions about exact copy, layout, styling, or motion, use the
  repository's product design skill when it has one.

### Security and performance

- Trace untrusted data from each entry point to the operations that use it.
  Check validation, output handling, authentication and authorization, secret
  exposure, destructive actions, and failure or retry behavior across trust
  boundaries.
- Check how work scales. Find N+1 calls, unbounded work or storage, missing
  pagination, leaked resources, blocking or repeated hot paths, and performance
  claims without measurement.
- Require every retry or poll loop to change something before its next attempt
  (backoff, refreshed state, or different input) and to stop at a bound. In a
  batch, one failing item must not block the rest.
- Flag only a reachable security problem or material performance cost introduced
  by the change.

### Optional omissions sweep

When the brief requests a sweep, reread the assigned diff and enclosing
functions after the first pass, looking only for defects absent from your
current findings. Focus on moved code that lost a guard, changed defaults,
and setup/teardown or acquisition/release asymmetry. Do not rederive existing
findings or repeat the full review. Verify new candidates yourself under
[Keep only supported findings](#keep-only-supported-findings), then return
one combined result. An empty sweep is valid; do not target a finding count.

## Keep only supported findings

Keep a finding only when all of these are true:

- It meaningfully affects requirements, correctness, security, performance, or
  maintainability.
- It is discrete and actionable.
- The reviewed change introduced it.
- The affected requirement, scenario, or call path can be demonstrated from
  the code and, for a specification finding, the cited specification.
- The author would probably fix it if they knew about it.

A style finding in changed lines needs only the last four conditions plus a
cited convention from the surrounding code or repository; report it as `P3`.

Reject speculation, pre-existing problems, intentional behavior within the
stated scope, and style preferences without a cited convention. Cite the
smallest useful range of changed lines for each finding. State the evidence,
affected scenario, impact, and smallest credible repair. Cite the exact source
and requirement for a specification or repository-rule finding. Return every
qualifying finding without padding or a numeric cap.

Use `$architecture-review` when the user wants a broad structural audit beyond
the selected change.

For pull requests, finish the independent review before reading existing review
discussion. Then inspect current checks and unresolved threads. The coordinating
agent posts findings only when the user explicitly asks; otherwise report them
locally.

## Repair before reporting

First, combine the review findings and decide which are supported. When the
user requested review only, report them without editing files. Otherwise, the
coordinating agent fixes every supported issue within the original task scope. Make these repairs one at a time. After an
implementation, this is the implementing agent's responsibility; a delegated
reviewer's findings are input to that work, not the final user response. Choose
the smallest supported repair and continue without asking the user to approve
the findings, choose routine implementation details, or authorize fixes already
covered by the task. Do not end the turn with a list of proposed fixes or an
offer to implement them.

Do not repair a finding that requires new authority or expands the original
task; report it unresolved and complete the other repairs.
Inspect the final diff before reporting the result. Do not start another review
after ordinary repairs. Start a new review only when
the user asks or the repairs materially change the original review scope.

## Report the result

Write findings and the summary with [Writing style](../../references/writing-style.md).

Present findings first, ordered by severity, marking each as repaired or
unresolved when repairs were requested or applied by default. Use one entry per
issue in this form:

`[P1] Imperative finding title — path/to/file.rs:line`

Follow the title with one short paragraph explaining the affected scenario and
why the behavior is wrong.

Use these priorities:

- `P0`: universal release blocker or critical failure.
- `P1`: urgent defect that should be fixed next.
- `P2`: ordinary defect that should be fixed.
- `P3`: low-impact issue that is still worth fixing.

If there are no qualifying findings, say `No findings.` After the findings, add
a brief overall assessment and mention any material test gaps or remaining
risks. Omit rejected candidates, descriptions of the review process, summaries
of areas without findings, and praise.

For repaired findings, summarize the applied fix and checks run. For unresolved
findings, state the blocker or decision needed from the user.
