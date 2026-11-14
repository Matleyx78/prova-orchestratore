"""Label as `ferma` the chains that stopped without saying so.

An open issue or pull request is a stuck chain when:
- the chain has started (a "Presa in carico" comment or a mention of an agent);
- it has none of the labels that mean "waiting for the owner" or "finished"
  (pronta, decisione, ferma, proposta);
- an issue is not handled by an open pull request that closes it;
- nothing has moved for at least SOGLIA_MINUTI minutes (and at most 24 hours:
  older items predate the sentinel and are left alone).

Environment: GITHUB_TOKEN, GITHUB_REPOSITORY, SOGLIA_MINUTI (default 30),
DRY_RUN=1 to only print.
"""

import datetime as dt
import json
import os
import re
import sys
import urllib.request

API = "https://api.github.com"
REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
SOGLIA = int(os.environ.get("SOGLIA_MINUTI", "30") or "30")
DRY_RUN = os.environ.get("DRY_RUN") == "1"
STOP_LABELS = {"pronta", "decisione", "ferma", "proposta"}
STARTED = re.compile(r"Presa in carico|@claude|@codex", re.IGNORECASE)
CLOSES = re.compile(r"(?:closes|fixes|resolves)\s+#(\d+)", re.IGNORECASE)


def call(method: str, path: str, body=None):
    req = urllib.request.Request(
        f"{API}{path}",
        method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read() or "null")


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc)
    items = call("GET", f"/repos/{REPO}/issues?state=open&per_page=100")
    handled_by_pr = set()
    for it in items:
        if "pull_request" in it:
            handled_by_pr.update(int(n) for n in CLOSES.findall(it.get("body") or ""))

    for it in items:
        number = it["number"]
        labels = {lab["name"] for lab in it["labels"]}
        is_pr = "pull_request" in it
        if labels & STOP_LABELS:
            continue
        if not is_pr and (number in handled_by_pr or not any(l.startswith("agente:") for l in labels)):
            continue
        updated = dt.datetime.fromisoformat(it["updated_at"].replace("Z", "+00:00"))
        idle = (now - updated).total_seconds() / 60
        if idle < SOGLIA or idle > 24 * 60:
            continue
        comments = call("GET", f"/repos/{REPO}/issues/{number}/comments?per_page=100")
        if not any(STARTED.search(c.get("body") or "") for c in comments):
            continue
        last = comments[-1] if comments else None
        held = "AA-Presa in carico" in labels
        text = (
            f"**Catena ferma** (sentinella): nessun movimento da {int(idle)} minuti"
            + (f"; ultimo commento di {last['user']['login']} alle {last['created_at'][11:16]} UTC" if last else "")
            + "."
            + ("\n\nL'etichetta `AA-Presa in carico` è rimasta: l'agente si è probabilmente interrotto"
               " (errore, tempo scaduto, quota). Toglila prima di riavviare." if held else "")
            + "\n\nPer riprendere: togli `ferma` e riavvia l'ultimo passaggio."
        )
        kind = "PR" if is_pr else "issue"
        print(f"{kind} #{number}: ferma da {int(idle)} min" + (" (AA rimasta)" if held else ""))
        if not DRY_RUN:
            call("POST", f"/repos/{REPO}/issues/{number}/labels", {"labels": ["ferma"]})
            call("POST", f"/repos/{REPO}/issues/{number}/comments", {"body": text})
    return 0


if __name__ == "__main__":
    sys.exit(main())
