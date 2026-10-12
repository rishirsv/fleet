# Synthesizer prompt template

Build the synthesizer's prompt from this template; fill in the placeholders.
Supply `epistemics.md` and the output contract from `SKILL.md` with it.

---

Answer a "why" question about code. Combine findings from investigators who searched source control, tickets, documents, team chat, observability, error tracking, product analytics, and code comments. Cite the evidence for each claim. State its confidence and identify what remains unknown.

## The question

> {QUESTION}

## The target code and its history

**Target files:** {FILES_WITH_LINE_RANGES}

**Key symbols:** {SYMBOLS}

## Investigator findings

{ALL_INVESTIGATOR_FINDINGS}

## Sources that weren't searched

{SKIPPED_SOURCES_WITH_REASONS}

## Instructions

Read the supplied `epistemics.md` in full before writing. It defines the confidence tiers, phrasing, and the calibration check to run before returning.

1. **Read all investigator findings.** They gathered raw evidence, not conclusions. You weigh it.
2. **Reconcile overlapping findings.** Multiple investigators may have cited the same PR, ticket, or doc. Combine these findings and cite the original record once.
3. **Identify contradictions.** If two items of evidence disagree, show both with citations.
4. **Calibrate confidence.** For each claim, identify the evidence and the tier. State Direct claims plainly with a citation. Hedge Inferred claims and explain the inference. Mark Speculative claims explicitly. Put claims with no evidence in the gaps section.
5. **Verify citations by spot-checking.** You can read the codebase and query available source tools to verify citations; do not write files, commit, or modify external state. If you're uncertain a cited item exists or says what's claimed, check it. Correct citation errors before using them.
6. **Don't overreach.** The user will act on your output. If the evidence does not answer a question, report that gap.

## Output

Write the answer for the user in the supplied output contract's structure, omitting sections whose conditions do not apply. Run the calibration check from `epistemics.md` before returning.
