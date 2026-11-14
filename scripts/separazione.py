"""Fail if a pull request mixes reference cases with other files.

A references pull request touches only tests/verifica/. A work pull request
may delete files in tests/verifica/in-attesa/ but must not touch the cases.
Usage: python3 scripts/separazione.py <base-sha> <head-sha>
"""

import subprocess
import sys


def main() -> int:
    base, head = sys.argv[1], sys.argv[2]
    out = subprocess.run(
        ["git", "diff", "--name-status", f"{base}...{head}"],
        check=True, capture_output=True, text=True,
    ).stdout
    changes = [line.split("\t") for line in out.splitlines() if line]
    paths = [c[-1] for c in changes]
    cases = [p for p in paths if p.startswith("tests/verifica/casi/")]
    others = [p for p in paths if not p.startswith("tests/verifica/")]
    if cases and others:
        print("Riferimenti mescolati con altri file:", *others, sep="\n  ")
        return 1
    print("Separazione dei riferimenti: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
