# Fleet's interactive shell. Keep non-interactive agent commands quiet.
[[ -o interactive ]] || return

# Preserve inherited PATH; discover portable user tools and Homebrew binaries.
typeset -U path PATH
path=($HOME/.local/bin $HOME/.bun/bin $HOME/.cargo/bin $path)
[[ ! -d /opt/homebrew/bin ]] || path=(/opt/homebrew/bin /opt/homebrew/sbin $path)
[[ ! -d /usr/local/bin ]] || path=(/usr/local/bin $path)

# Machine-specific exports and secrets stay outside Git.
[[ ! -f "$HOME/.zshrc.local" ]] || source "$HOME/.zshrc.local"

# Allow Codex and other shell-launched tools to open more files.
ulimit -S -n 4096

HISTFILE="${ZDOTDIR:-$HOME}/.zsh_history"
HISTSIZE=20000
SAVEHIST=20000
setopt APPEND_HISTORY HIST_IGNORE_ALL_DUPS HIST_IGNORE_SPACE HIST_REDUCE_BLANKS

autoload -Uz compinit
compinit
bindkey -e
autoload -Uz up-line-or-beginning-search down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search
bindkey '^[[A' up-line-or-beginning-search
bindkey '^[[B' down-line-or-beginning-search

# No Git subprocess on every prompt; agents can inspect status explicitly.
PROMPT='%F{cyan}%~%f %(?.%F{green}.%F{red})❯%f '
RPROMPT=''

# Agent shortcuts pass arguments unchanged and retain each tool's permissions.
function cx { command codex "$@"; }
function cxp { CODEX_HOME="$HOME/.codex-personal" command codex "$@"; }
function cl { command claude "$@"; }

# Explicit Git inspection; avoid aliases for destructive or publishing commands.
function gs { command git status --short --branch "$@"; }
function gd { command git diff "$@"; }
function gds { command git diff --cached "$@"; }
function gr {
  local root
  root="$(command git rev-parse --show-toplevel)" || return
  cd "$root"
}

# Preview by default. Set FLEET_HOME in ~/.zshrc.local for another checkout path.
function fleet {
  local repo="${FLEET_HOME:-$HOME/Code/fleet}"
  if [[ ! -x "$repo/scripts/sync-configs.sh" ]]; then
    print -u2 'Fleet checkout not found. Set FLEET_HOME in ~/.zshrc.local.'
    return 1
  fi
  "$repo/scripts/sync-configs.sh" "$@"
}
