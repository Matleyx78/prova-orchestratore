#!/usr/bin/env bash
# Create the labels and the test issues described in prove/issue/*.md.
# Each file starts with "etichetta: <label>" and "titolo: <title>", then a
# blank line and the issue body. Issues whose title already exists are skipped.
# Usage: scripts/apri-prove.sh
set -euo pipefail

repo="Matleyx78/prova-orchestratore"
dir="$(cd "$(dirname "$0")/.." && pwd)/prove/issue"

make_label() {
  gh api "repos/$repo/labels" -f name="$1" -f color="$2" -f description="$3" \
    --silent 2>/dev/null && echo "label created: $1" || echo "label exists: $1"
}

make_label "agente:claude" "d97757" "Issue assegnata a Claude"
make_label "agente:codex" "10a37f" "Issue assegnata a Codex"
make_label "AA-Presa in carico" "fbca04" "Un agente ci sta lavorando"

existing="$(gh api "repos/$repo/issues?state=all&per_page=100" --jq '.[].title')"

for file in "$dir"/*.md; do
  label="$(sed -n 's/^etichetta: //p' "$file" | head -n 1)"
  title="$(sed -n 's/^titolo: //p' "$file" | head -n 1)"
  body="$(sed '1,3d' "$file")"
  if grep -Fxq "$title" <<<"$existing"; then
    echo "issue exists: $title"
    continue
  fi
  gh api "repos/$repo/issues" -f title="$title" -f body="$body" \
    -f "labels[]=$label" --jq '"issue #" + (.number|tostring) + ": " + .title'
done
