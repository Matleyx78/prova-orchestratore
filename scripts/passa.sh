#!/usr/bin/env bash
# Hand a pull request over to the other agent with a mention written as the
# owner: the agents only answer comments from the owner.
# Uses GH_TOKEN_UTENTE if set (Claude in GitHub Actions), otherwise GH_TOKEN
# (Codex, whose token already belongs to the owner).
# Usage: scripts/passa.sh <claude|codex> <pr-number> <revisione|correzioni|analisi> [round]
set -euo pipefail

usage() {
  echo "usage: $0 <claude|codex> <pr-number> <revisione|correzioni|analisi> [round]" >&2
  exit 2
}

[ $# -ge 3 ] || usage
agent="$1" pr="$2" kind="$3" round="${4:-}"
case "$pr" in ''|*[!0-9]*) usage;; esac

case "$agent" in
  claude) prefix="@claude [modello: opus] [impegno: alto]" ;;
  codex) prefix="@codex Prima di tutto esegui git fetch origin." ;;
  *) usage ;;
esac

case "$kind" in
  revisione|correzioni)
    case "$round" in ''|*[!0-9]*) usage;; esac ;;
  analisi) ;;
  *) usage ;;
esac

case "$kind" in
  revisione)
    task="Rivedi questa pull request come dice AGENTS.md in \"Revisione (revisore)\" (giro $round)." ;;
  correzioni)
    task="Correggi le segnalazioni bloccanti del giro di revisione $round (e della ripresa dopo la decisione, se c'è) come dice AGENTS.md in \"Correzioni (esecutore)\"." ;;
  analisi)
    task="La CI di questa pull request non passa dopo tre tentativi: analizzala come dice AGENTS.md in \"Analisi di una CI rossa (revisore)\"." ;;
esac

token="${GH_TOKEN_UTENTE:-${GH_TOKEN:-}}"
if [ -z "$token" ]; then
  echo "neither GH_TOKEN_UTENTE nor GH_TOKEN is set" >&2
  exit 1
fi

body="$prefix Leggi AGENTS.md e seguilo alla lettera. $task"
GH_TOKEN="$token" gh api "repos/Matleyx78/prova-orchestratore/issues/$pr/comments" \
  -f body="$body" --jq '.html_url'
