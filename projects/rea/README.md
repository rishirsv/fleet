# REA source in Fleet

The complete upstream REA source snapshot is bundled in the installable plugin:
[rea-6.7.0-source.zip](../../plugins/rea/runtime/rea-6.7.0-source.zip).
[origin.json](../../plugins/rea/runtime/origin.json) records its upstream repository,
commit, version and archive SHA-256. This supplied main-branch snapshot is not
assumed byte-identical to the published npm release.

Fleet builds and runs this source. See the [plugin setup guide](../../plugins/rea/README.md)
for the single new-computer command, separately installed dependencies, build
layout and protection for existing installations. The archive includes upstream
instructions and development skills; they do not become Fleet setup commands or
additional active plugin skills. Fleet maintains its active skills in `plugins/rea/skills/`.

For upstream development, extract a separate working copy and read its own
`AGENTS.md` and `CONTRIBUTING.md`. Do not edit ignored build generations or installed
caches as maintained source. The upstream MIT license and third-party notices
remain in the source archive, with the plugin license alongside the package.
