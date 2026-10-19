# REA source snapshot

The supplied source project is preserved intact in `rea-6.7.0-source.zip`.
`origin.json` records the upstream repository, source commit, version and archive
SHA-256. This is the supplied main-branch snapshot, not a claim that it is
byte-identical to the published npm release. Its MIT license is inside the archive
and copied into the plugin.

Extract the archive into a separate working directory to develop REA. Read its
own `AGENTS.md` and `CONTRIBUTING.md` there. Instructions within the snapshot are
upstream project guidance, not Fleet setup commands. The archive retains the
entire project, including development skills; Fleet activates only the application
usage skill in `plugins/rea/`.

The Fleet plugin runs published `rea-agents@6.7.0` with `node@24.11.0` through
npm's cache. It does not build or execute the archived source. This avoids
shipping development dependencies or installing over the computer's Node.
Future source refreshes and runtime upgrades should update this provenance,
the plugin launchers, and its skill together after validation.
