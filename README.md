# prova-orchestratore

Repository usa e getta per capire se il flusso degli agenti di Tecnigrafo e
solid-space si può automatizzare: un'automazione che scrive `@claude` o
`@codex` nelle issue e nelle pull request, e gli agenti che partono da soli.

Qui non si sviluppa niente di vero: `src/calc.py` è una funzione banale con i
suoi test, e serve solo a dare agli agenti un lavoro piccolo, con una CI che
può diventare verde o rossa.

## Che cosa c'è

| File | A che cosa serve |
|---|---|
| `AGENTS.md`, `CLAUDE.md` | Regole ridotte di Tecnigrafo: presa in carico, PR, CI, revisione |
| `.github/workflows/ci.yml` | Test Python a ogni push e pull request |
| `.github/workflows/claude.yml` | Avvia Claude quando un commento contiene `@claude` (piano Max) |
| `.github/workflows/relay.yml` | Prova 3: scrive un commento con `@claude` o `@codex` come automazione |
| `scripts/ci-attendi.sh` | Attesa della CI con un solo comando che blocca |

## Preparazione (una volta sola)

1. **App di Claude.** Installa <https://github.com/apps/claude> solo su questo
   repository.
2. **Token di Claude.** Nel Debian in WSL lancia `claude setup-token` e
   accedi con l'account del piano Max. Copia il token (`sk-ant-oat01-…`) in
   *Settings → Secrets and variables → Actions → New repository secret*, con
   nome `CLAUDE_CODE_OAUTH_TOKEN`.
3. **Codex.** Nelle impostazioni di Codex sul web crea un ambiente per questo
   repository e attiva, se c'è, l'opzione che fa rispondere Codex alle
   menzioni su GitHub.
4. **Token personale, per la prova 3.** In *GitHub → Settings → Developer
   settings → Fine-grained tokens* creane uno valido solo per questo
   repository, con *Issues* e *Pull requests* in lettura e scrittura. Mettilo
   nel secret `RELAY_PAT`.
5. **GitHub App, per la prova 3 (si può rimandare).** In *Developer settings →
   GitHub Apps → New GitHub App*: nome a scelta, webhook disattivato, permessi
   *Issues* e *Pull requests* in lettura e scrittura, installabile solo sul tuo
   account. Installala su questo repository. Metti l'*App ID* nella variabile
   `RELAY_APP_ID` (scheda *Variables*) e la chiave privata (file `.pem`) nel
   secret `RELAY_APP_PRIVATE_KEY`.

Le prove, una per una, sono in `docs/PROVE.md`.
