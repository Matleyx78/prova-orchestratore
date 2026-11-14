#!/usr/bin/env bash
# Ask Codex to fix a pull request after a review, writing the comment with the
# owner's token (GH_TOKEN_UTENTE): Codex does not answer comments from bots.
# Usage: scripts/passa-a-codex.sh <pr-number> <round>
set -euo pipefail

if [ $# -ne 2 ]; then
  echo "usage: $0 <pr-number> <round>" >&2
  exit 2
fi
case "$1$2" in ''|*[!0-9]*) echo "pr-number and round must be numbers" >&2; exit 2;; esac
if [ -z "${GH_TOKEN_UTENTE:-}" ]; then
  echo "GH_TOKEN_UTENTE is not set" >&2
  exit 1
fi

body="@codex Prima di tutto esegui git pull --ff-only origin main. Leggi AGENTS.md e seguilo alla lettera. Correggi le segnalazioni bloccanti del giro di revisione $2 di questa pull request come dice AGENTS.md in \"Correzioni\"."
GH_TOKEN="$GH_TOKEN_UTENTE" gh api "repos/Matleyx78/prova-orchestratore/issues/$1/comments" \
  -f body="$body" --jq '.html_url'
