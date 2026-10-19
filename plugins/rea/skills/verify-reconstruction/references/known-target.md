# A known target for calibration

Use this exercise when the user requests practice or tool calibration, not as a
prerequisite to analyzing their artifact. Create a separate scratch directory;
keep source, samples, notes, evidence and tests apart.

This guide includes the answer key. For a blind exercise, give a fresh analyst
only the compiled artifact and the behavior question, withholding this guide and
the source until its specification is recorded. If the analyst already saw the
answer, describe the result as tool calibration rather than blind recovery.

Compile [record.c](../assets/record.c) with an available C compiler at `-O2` into
the scratch directory. Record the compiler, flags, architecture, binary digest
and reference output. Keep the source out of the analyst's initial evidence.
Inspect only the compiled `checksum` and `valid_record` routines and their
necessary callers. Infer the spec, then compare it to source and execution.

The answer key is a 32-bit FNV-1a recurrence and a parser that accepts lengths
of at least four, magic bytes `RE`, version 1, and byte 3 at most 32. Test lengths
0–3, exactly 4, wrong magic/version, byte 3 values 31/32/33/128/255 and trailing
bytes. For checksum, include empty input, zero bytes and high-bit bytes; use
independent published vectors or the retained source oracle to grade predictions.
The program's default output is only a smoke test: extend a separate harness to
exercise these functions rather than claiming it covers those cases.

After the first pass, strip a copy using the host's available tooling. Preserve
the original and separately record the stripped digest; keep the answer key away
from the analyst until its hypotheses are recorded. Compare recovered semantics
and missed functions across builds. Never strip the sole original artifact.
