#!/usr/bin/env zsh
set -euo pipefail

ROOT="${0:A:h:h}"
source "$ROOT/scripts/plugin-sync/source.sh"
MODE=apply
DRY_RUN=1
PROFILE=""
TARGETS=()

usage() {
  cat <<'EOF'
Usage: scripts/sync-configs.sh [--dry-run|--apply|--status] [--agents|--codex|--claude|--vscode|--karabiner|--ghostty|--zsh|--spaces ...] [--profile PATH]

Preview by default. Selected targets cover Codex, Claude, VS Code, Karabiner,
Ghostty, and Zsh. Merge Fleet's Codex settings into CODEX_HOME (or ~/.codex)
and ~/.codex-personal when present. --profile selects just one profile.
Each profile retains its cloud/local Dots/Drafts policy and machine-local state.
Apply validates settings and backs up existing config before writing.
Sync also merges shared agent guidance and installs selected VS Code extensions.
Codex/Claude plugin installation uses sync-plugins.sh. Sync does not push Git
or contact other computers. --profile scopes Codex settings and guidance only.
EOF
}

while (( $# )); do
  case "$1" in
    --dry-run) MODE=apply; DRY_RUN=1 ;;
    --apply) MODE=apply; DRY_RUN=0 ;;
    --status) MODE=status; DRY_RUN=0 ;;
    --agents|--codex|--claude|--vscode|--karabiner|--ghostty|--zsh|--spaces) TARGETS+=("${1#--}") ;;
    --profile)
      (( $# >= 2 )) || { usage >&2; exit 2; }
      PROFILE="$2"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) usage >&2; exit 2 ;;
  esac
  shift
done
(( ${#TARGETS} )) || TARGETS=(agents codex claude vscode karabiner ghostty zsh spaces)

if (( ${TARGETS[(Ie)codex]} )); then
  command -v uv >/dev/null || { echo 'uv is required for Codex sync' >&2; exit 2; }
fi
profiles=("${CODEX_HOME:-$HOME/.codex}")
if [[ -n "$PROFILE" ]]; then
  profiles=("$PROFILE")
elif [[ -d "$HOME/.codex-personal" && "${profiles[1]}" != "$HOME/.codex-personal" ]]; then
  profiles+=("$HOME/.codex-personal")
fi

result=0
if (( ${TARGETS[(Ie)agents]} )); then
  guidance_targets=("${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md")
  for profile in "${profiles[@]}"; do
    guidance_targets+=("$profile/AGENTS.md")
  done
  for target in "${guidance_targets[@]}"; do
    args=("$MODE" --source "$ROOT/configs/agents/AGENTS.md" --target "$target")
    (( ! DRY_RUN )) || args+=(--dry-run)
    python3 "$ROOT/scripts/config-sync.py" "${args[@]}" --format guidance || result=$?
  done
fi
if (( ${TARGETS[(Ie)codex]} )); then
for profile in "${profiles[@]}"; do
  policy="$(codex_plugin_source "$profile")"
  # One combined source makes base settings and profile policy one validated,
  # atomic config update rather than two partially applied writes.
  source_file="$(mktemp "${TMPDIR:-/tmp}/fleet-codex-config.XXXXXX")"
  trap 'rm -f "$source_file"' EXIT
  cat "$ROOT/configs/codex/config.toml" > "$source_file"
  printf '\n' >> "$source_file"
  cat "$policy" >> "$source_file"
  args=("$MODE" --source "$source_file" --target "$profile/config.toml")
  (( ! DRY_RUN )) || args+=(--dry-run)
  uv run --quiet --script "$ROOT/scripts/plugin-sync/merge-codex-config.py" "${args[@]}" || result=$?
  rm -f "$source_file"
  args=("$MODE" --browser --source "$ROOT/configs/codex/browser.toml" --target "$profile/browser/config.toml")
  (( ! DRY_RUN )) || args+=(--dry-run)
  uv run --quiet --script "$ROOT/scripts/plugin-sync/merge-codex-config.py" "${args[@]}" || result=$?
  if [[ -f "$ROOT/configs/codex/keybindings.json" ]]; then
    args=("$MODE" --source "$ROOT/configs/codex/keybindings.json" --target "$profile/keybindings.json")
    (( ! DRY_RUN )) || args+=(--dry-run)
    python3 "$ROOT/scripts/config-sync.py" "${args[@]}" --format codex-keys || result=$?
  fi
done
fi
if (( ${TARGETS[(Ie)claude]} )); then
  args=("$MODE" --source "$ROOT/configs/claude/settings.json" --target "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json")
  (( ! DRY_RUN )) || args+=(--dry-run)
  python3 "$ROOT/scripts/config-sync.py" "${args[@]}" || result=$?
  args=("$MODE" --source "$ROOT/configs/claude/keybindings.json" --target "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/keybindings.json" --format claude-keys)
  (( ! DRY_RUN )) || args+=(--dry-run)
  python3 "$ROOT/scripts/config-sync.py" "${args[@]}" || result=$?
fi
if (( ${TARGETS[(Ie)vscode]} )); then
  if [[ "$(uname -s)" == Darwin ]]; then
    vscode_dir="${VSCODE_USER_DIR:-$HOME/Library/Application Support/Code/User}"
  else
    vscode_dir="${VSCODE_USER_DIR:-${XDG_CONFIG_HOME:-$HOME/.config}/Code/User}"
  fi
  for file in settings keybindings; do
    args=("$MODE" --source "$ROOT/configs/vscode/$file.json" --target "$vscode_dir/$file.json")
    [[ "$file" != keybindings ]] || args+=(--format vscode-keys)
    (( ! DRY_RUN )) || args+=(--dry-run)
    python3 "$ROOT/scripts/config-sync.py" "${args[@]}" || result=$?
  done
  args=("$MODE" --source "$ROOT/configs/vscode/extensions.json")
  (( ! DRY_RUN )) || args+=(--dry-run)
  python3 "$ROOT/scripts/config-sync.py" "${args[@]}" --format extensions || result=$?
fi
if (( ${TARGETS[(Ie)karabiner]} )) && [[ "$(uname -s)" == Darwin ]]; then
  args=("$MODE" --source "$ROOT/configs/karabiner/hyper.json" --target "${XDG_CONFIG_HOME:-$HOME/.config}/karabiner/karabiner.json" --format karabiner)
  (( ! DRY_RUN )) || args+=(--dry-run)
  python3 "$ROOT/scripts/config-sync.py" "${args[@]}" || result=$?
fi
font_source="$ROOT/configs/fonts/paper-mono/PaperMono-Regular.otf"
font_target="$HOME/Library/Fonts/PaperMono-Regular.otf"
if (( ${TARGETS[(Ie)codex]} || ${TARGETS[(Ie)vscode]} || ${TARGETS[(Ie)ghostty]} )) && [[ "$(uname -s)" == Darwin && -f "$font_source" ]]; then
  if [[ ! -f "$font_target" ]] || ! cmp -s "$font_source" "$font_target"; then
    if [[ "$MODE" == status ]]; then
      echo "Drift $font_target"; result=1
    elif (( DRY_RUN )); then
      echo "Would install $font_target"
    elif (( result == 0 )); then
      mkdir -p "${font_target:h}"
      [[ ! -e "$font_target" ]] || cp -p "$font_target" "$font_target.bak.$(date +%Y%m%d%H%M%S)"
      cp -p "$font_source" "$font_target"
    fi
  fi
fi

install_file() {
  local source="$1" target="$2"
  [[ -f "$source" ]] || return 0
  if [[ -f "$target" && ! -L "$target" ]] && cmp -s "$source" "$target"; then
    echo "Current $target"
  elif [[ "$MODE" == status ]]; then
    echo "Drift $target"; result=1
  elif (( DRY_RUN )); then
    echo "Would install $source -> $target"
  else
    mkdir -p "${target:h}"
    if [[ -e "$target" || -L "$target" ]]; then
      cp -pP "$target" "$target.bak.$(date +%Y%m%d%H%M%S)"
      rm -f "$target"
    fi
    cp -p "$source" "$target"
  fi
}
if (( result == 0 || DRY_RUN )) || [[ "$MODE" == status ]]; then
  if (( ${TARGETS[(Ie)ghostty]} )); then
    install_file "$ROOT/configs/ghostty/config.ghostty" "${XDG_CONFIG_HOME:-$HOME/.config}/ghostty/config.ghostty"
  fi
  if (( ${TARGETS[(Ie)zsh]} )); then
    install_file "$ROOT/configs/zsh/.zshrc" "${ZDOTDIR:-$HOME}/.zshrc"
  fi
fi
if (( ${TARGETS[(Ie)spaces]} )); then
  args=("$MODE")
  (( ! DRY_RUN )) || args+=(--dry-run)
  python3 "$ROOT/scripts/sync-spaces.py" "${args[@]}" || result=$?
  python3 "$ROOT/scripts/logi-options/sync-spaces.py" "${args[@]}" || result=$?
fi
exit "$result"
