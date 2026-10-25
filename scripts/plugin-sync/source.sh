# Shared by plugin and config sync. Selection is local to each Codex profile.
codex_plugin_source() {
  local profile_home="$1" selection_file="$1/pstack-plugin-source" selection=local
  # Read the previous marker until this profile's next plugin sync migrates it.
  [[ -f "$selection_file" || ! -f "$profile_home/dots-plugin-source" ]] || selection_file="$profile_home/dots-plugin-source"
  [[ ! -f "$selection_file" ]] || selection="$(<"$selection_file")"
  case "$selection" in
    cloud) echo "$ROOT/scripts/plugin-sync/plugins-cloud.toml" ;;
    local) echo "$ROOT/scripts/plugin-sync/plugin-exclusions.toml" ;;
    *) echo "Invalid plugin source in $selection_file: $selection" >&2; return 2 ;;
  esac
}
