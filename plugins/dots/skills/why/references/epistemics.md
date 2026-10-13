# Epistemics

Use these rules to assess and communicate confidence in historical evidence. Keep uncertainty visible when records are incomplete or contradictory.

Contents: [Confidence tiers](#confidence-tiers) · [Phrasing guide](#phrasing-guide) · [Check the user's hypothesis](#check-the-users-hypothesis) · [When evidence contradicts](#when-evidence-contradicts) · [When evidence is missing](#when-evidence-is-missing) · [Calibration check before finalizing](#calibration-check-before-finalizing)

Code shows what it does. To establish why it exists, inspect commits, PRs, tickets, documents, and conversations. Those records can be incomplete, biased, or missing. Do not present an interpretation of code as recorded intent.

## Confidence tiers

Every claim in the final output must have one of these confidence tiers. The tier determines which output section the claim goes in and how it's phrased.

### 1. Direct

An explicit, textual citation that answers the question. Not "the code does X so the author must have wanted X." Something an author actually *wrote* that says why.

Examples:
- A PR description that says "this fixes the bug where users with >1000 items couldn't paginate"
- A ticket that says "we're adding this because customer Acme requested it in their security review"
- A code comment that says "// clamp to 100 because the upstream API rejects larger values"
- A design doc that says "we chose option A over option B because we need persistence across restarts"
- A chat message from the author saying "switching to this approach since the old one was flaky in tests"

Phrasing: confident, present tense. "This exists because X." Cite the source.

### 2. Supported

Multiple pieces of indirect evidence converge. No single source states it explicitly, but the pattern across sources makes it likely.

Examples:
- The PR title says "improve performance," the ticket is labeled "perf," and the surrounding commits all touch the same hot path
- Multiple tests were added alongside the change, all exercising edge cases with very large inputs
- The author's other PRs from the same week all mention the same incident in their descriptions

Phrasing: confident but clearly derived. "The evidence points strongly to X: [the specific pieces]." Cite multiple sources.

### 3. Inferred

A reasonable reading of the context, but nothing explicitly supports it. The reader should understand this is *your interpretation*, not a fact from the record.

Examples:
- The PR doesn't say why, but given the error was happening in production (per the incident channel timing) and the fix was rushed (merged the same day), it was likely a hotfix.
- The function name suggests retry logic; the retry count is 3; this matches the team's general convention of "3 retries" seen elsewhere in the codebase.

Phrasing: hedged. "It appears", "likely", "suggests", "is consistent with", "one reading is". Make the inference chain explicit: "Given A and B, C seems likely because D."

### 4. Speculative

A plausible hypothesis, but the evidence is thin and other explanations fit equally well. Presenting these is valuable, but mark them clearly as guesses.

Examples:
- "This might be a workaround for a browser bug that's since been fixed, but we found no contemporary evidence of that."
- "It's possible this threshold was chosen to match an SLA commitment, but no SLA doc references it."

Phrasing: explicitly speculative. "One possibility is X, but we have no direct evidence." Usually lives in the "Competing hypotheses" section alongside other possibilities.

### 5. Unknown

You looked and couldn't find out. A valid and important outcome. Document it.

Phrasing: "We searched X, Y, and Z and found no evidence of why." Be specific about *what* you searched. "We couldn't find out" is less useful than "we searched the ticket tracker with keywords A and B, scanned the 6 PRs that touched this file since 2023, and grep'd the repo for string literals matching the threshold; none surfaced a rationale."

## Phrasing guide

**Confidence words** imply Direct or Supported evidence and need a citation immediately adjacent. Never use them for inferences: "because", "the reason is", "was designed to" (claims author intent), "fixes" / "addresses" / "solves" (claims the change achieved its goal), "the team decided" (claims a group decision happened).

**Hedges** signal interpretation, not report. Use them in "What we can reasonably infer": "appears to", "seems to", "likely", "suggests", "is consistent with", "one reading is", "plausibly", "may have been", "the evidence points toward".

### Words to avoid

- "obviously". If it were obvious, the user wouldn't be asking
- "clearly". Almost always precedes a claim that isn't clear
- "of course". Same
- "just" (as in "it's just X for performance"). Dismissive and usually hides uncertainty
- "I think" / "I believe". You're synthesizing evidence, not giving a personal opinion. Use "the evidence suggests" instead.

### Avoid rationalization

Code that "makes sense" today may have been written for reasons that no longer apply, or that were wrong at the time. Don't retrofit a present-day justification onto uncertain history, assume the author did the "right" thing and work backward, assume a consistent pattern was intentional when it might be copy-paste, or turn an absence of evidence into evidence of absence ("no one mentioned security concerns, so it must not have been a concern").

## Check the user's hypothesis

Users often phrase `why` questions with an embedded hypothesis: "Why do we do it this way, I assume it's for performance?" Check that hypothesis against the evidence. Treat it as one candidate among others and check the evidence independently. If the evidence supports it, say so with citations; if not, say so and present what the evidence *does* support.

Treat the user's guess as a prompt for investigation.

## When evidence contradicts

If two sources disagree (the PR description says one thing, the ticket says another), surface both. Do not discard a source because it conflicts with the proposed explanation. A typical pattern:

- **The ticket says** "we need this for customer X's compliance requirement"
- **The PR says** "cleaning up tech debt in this area"

Both may be true (the ticket motivated the work, the PR is the author's framing of it), or one may be wrong. Present both with their citations so the user can assess the conflict.

## When evidence is missing

Failing to mark a gap and filling it with a confident guess harms the user, because they'll act on the guess. An honest "we don't know" tells them the answer isn't in the obvious places and that they need to ask a human or drop the question. Name each gap concretely: the question, the sources searched, what you searched for in each, and what you found (nothing, or only tangential material).

## Calibration check before finalizing

Whoever writes the final answer, directly or as the synthesizer, reviews every claim in "What we found" and "What we can reasonably infer" before returning it:

1. Does this claim have a citation? If not, add one or move it to "Inferred" or "Competing hypotheses".
2. Is the phrasing calibrated to the tier? A Direct claim can use "because"; an Inferred claim cannot. Do not state weakly supported claims with confidence.
3. Does the answer treat the code itself as evidence for its own intent? Code shows behavior; it does not prove motivation. Remove or reclassify the claim.
4. Are contradictions shown with both citations, instead of one side being quietly chosen?
5. If the user embedded a hypothesis in the question, was it checked against the evidence?
6. Does "What we do not know" name each material gap? Omit the section only when the searched evidence answers every material question; do not invent a gap to fill it.

If any item fails, revise before returning.
