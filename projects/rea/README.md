# REA in Fleet

The full upstream source lives in [plugins/rea](../../plugins/rea/README.md).
Fleet packages it without modifying upstream files or adding investigation skills.

See the [Fleet packaging guide](../../plugins/rea/fleet/README.md) for the
one-command new-computer setup, upstream refresh command, provenance and separately
installed dependencies. The installed/cached copies remain independent until an
explicit migration or Fleet sync.
