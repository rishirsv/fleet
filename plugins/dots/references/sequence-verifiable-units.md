# Sequence work into verifiable units

Read for a migration, sweep, or run of similar edits where later work depends
on an earlier change. A unit is a coherent behavior or dependency boundary,
not necessarily one file or call site.

Order work as a sequence of small units, each ending in a state you can check,
and don't advance dependent work until the current unit is green.

**Why:** A break caught at the unit that caused it is cheap to localize. A break
caught after a batch is buried, and you have already built further on a broken
base. Sequencing those same units into a delivery a reviewer can replay turns
"trust me" into "watch it go red, then green."

**Execution.** Each unit is a before/after bracket: known-good state, one change,
run the check, then proceed. Use the narrow check that proves the unit's
contract; batch mechanically identical independent edits when the same check
covers them. Reuse passing evidence until a later change invalidates it.
Do not rerun the full suite or request another review for every unit.
If the baseline already fails, distinguish that failure before attributing a
result to the change. Resolve or report a failed prerequisite before building
on it.

**Delivery.** When commits or PRs are requested, stack them in the order that
proves the work. Story orders include a subtraction before the reshape, a
baseline capture before the treatment, the scaffold before the feature.
Respect repository requirements for independently passing commits; a failing
regression control may be recorded as evidence within the fix rather than
landed on its own. This reference does not authorize rebasing, committing,
pushing, or publishing.
