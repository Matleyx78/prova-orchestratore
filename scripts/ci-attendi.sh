#!/usr/bin/env bash
# Wait for all CI checks of a pull request with one blocking command.
# Usage: scripts/ci-attendi.sh <pr-number>
# Exit code: 0 if every check passed, non-zero otherwise.
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: $0 <pr-number>" >&2
  exit 2
fi

# Checks may take a few seconds to appear after the push.
sleep 20
gh pr checks "$1" --watch --interval 20
