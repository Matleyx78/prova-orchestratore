#!/usr/bin/env bash
# Start (or resume) the work on an issue, writing the mention as the owner.
# The agent is the one of the issue's "agente:" label.
# Usage: scripts/avvia.sh <issue-number> <reason>
set -euo pipefail

repo="Matleyx78/prova-orchestratore"
issue="${1:-}" reason="${2:-}"
case "$issue" in ''|*[!0-9]*) echo "usage: $0 <issue-number> <reason>" >&2; exit 2;; esac

token="${GH_TOKEN_UTENTE:-${GH_TOKEN:-}}"
[ -n "$token" ] || { echo "neither GH_TOKEN_UTENTE nor GH_TOKEN is set" >&2; exit 1; }

agent="$(gh api "repos/$repo/issues/$issue" --jq '[.labels[].name|select(startswith("agente:"))][0] // "" | sub("agente:";"")')"
case "$agent" in
  claude) prefix="@claude [modello: opus] [impegno: medio]" ;;
  codex) prefix="@codex Prima di tutto esegui git fetch origin." ;;
  *) echo "issue #$issue has no agente: label" >&2; exit 1 ;;
esac

# A resumed issue is no longer waiting for a decision.
gh api -X DELETE "repos/$repo/issues/$issue/labels/decisione" >/dev/null 2>&1 || true

body="$prefix Leggi AGENTS.md e seguilo alla lettera. $reason Realizza questa issue, o riprendila da dove si era fermata."
GH_TOKEN="$token" gh api "repos/$repo/issues/$issue/comments" -f body="$body" --jq '.html_url'
