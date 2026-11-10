# Le prove

Obiettivo: sapere se un'automazione può avviare Claude e Codex scrivendo
`@claude` e `@codex` nelle issue e nelle pull request, e se gli agenti, avviati
così, seguono da soli AGENTS.md fino alla CI verde.

Le issue si creano con `scripts/apri-prove.sh` (lo lancia Claude o tu, una
volta sola). Ogni issue usa file suoi, quindi le prove possono girare anche
insieme senza conflitti. Dopo ogni prova guarda:

- **Actions**, per Claude: il workflow *Claude* è partito? È finito senza
  errori?
- **Codex sul web**, per Codex: è comparso un lavoro nuovo?
- **la issue**: etichetta `AA-Presa in carico` messa e poi tolta, commento di
  presa in carico, pull request con `Closes #N`, CI verde, riepilogo.
- **i consumi**: per Claude, l'uso nelle impostazioni di claude.ai deve
  crescere e non deve esserci spesa API; per Codex, i limiti nelle sue
  impostazioni.

## Prova 1: Codex risponde a una tua menzione (issue P1)

Prerequisito: README, passo 3. Nella issue **[P1]** scrivi tu:

```text
@codex Leggi AGENTS.md e seguilo alla lettera. Realizza questa issue.
```

Da annotare: Codex parte? Apre la pull request da solo, o serve un clic su
«Create PR» nel sito di Codex? Mette e toglie l'etichetta? Aspetta la CI?

## Prova 2: Claude risponde a una tua menzione (issue P2)

Prerequisiti: README, passi 1 e 2. Nella issue **[P2]** scrivi tu:

```text
@claude Leggi AGENTS.md e seguilo alla lettera. Realizza questa issue.
```

Da annotare: il workflow parte? Claude prende in carico, apre la pull
request, aspetta la CI con `scripts/ci-attendi.sh` e si ferma al verde? Il
consumo va sul piano Max?

## Prova 3: l'automazione scrive la menzione (issue P3a–P3d)

È la prova che decide. Si fa con il workflow *Relay* (*Actions → Relay → Run
workflow*): numero della issue, agente, identità, messaggio predefinito.

| Issue | Agente | Identità | Prerequisito |
|---|---|---|---|
| P3a | claude | prima `github_token`, poi `pat` | README, passo 4 |
| P3b | claude | `app` | README, passo 5 |
| P3c | codex | prima `github_token`, poi `pat` | README, passo 4 |
| P3d | codex | `app` | README, passo 5 |

Con `github_token` ci si aspetta che **non** parta niente: è il controllo che
la prova distingue davvero i casi. Aspetta qualche minuto prima di passare a
`pat` sulla stessa issue.

Da annotare: per ogni riga, l'agente parte sì o no. Con `pat` il commento
appare a nome tuo; con `app` a nome dell'app, ed è la soluzione più pulita per
un orchestratore vero.

## Prova 4: revisione incrociata e correzione

Sulla pull request della prova 2 (di Claude), con il workflow *Relay* e
l'identità che ha funzionato nella prova 3, agente `codex`, messaggio:

```text
Leggi AGENTS.md e seguilo alla lettera. Rivedi questa pull request come dice AGENTS.md in "Revisione".
```

Poi, sulla stessa pull request, agente `claude`, messaggio:

```text
Leggi AGENTS.md e seguilo alla lettera. Correggi le segnalazioni della revisione come dice AGENTS.md in "Correzioni".
```

Ripeti a parti invertite sulla pull request della prova 1 (di Codex). Se la
revisione non ha segnalazioni, chiedine una apposta: «segnala almeno un
miglioramento possibile».

Da annotare: la revisione arriva come un solo commento, senza commit? La
correzione tocca solo ciò che è stato segnalato e riporta la CI al verde?

## Esiti

| Prova | Parte? | Segue AGENTS.md? | Note |
|---|---|---|---|
| 1. Codex, menzione tua | | | |
| 2. Claude, menzione tua | | | |
| 3a. Claude, `github_token` | | — | atteso: no |
| 3a. Claude, `pat` | | | |
| 3b. Claude, `app` | | | |
| 3c. Codex, `github_token` | | — | atteso: no |
| 3c. Codex, `pat` | | | |
| 3d. Codex, `app` | | | |
| 4. Revisione Codex → correzione Claude | | | |
| 4. Revisione Claude → correzione Codex | | | |

Se le prove 3 e 4 riescono con almeno un'identità per agente,
l'orchestratore si può fare. Se no, ci si ferma qui.
