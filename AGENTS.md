# Istruzioni per agenti IA

Repository di prova. Le regole sono una versione ridotta di quelle di
Tecnigrafo: servono a vedere se un agente avviato da GitHub le segue da solo.

## Per prima cosa: prendi in carico

Su una issue o pull request che esiste già, **subito**, prima di modificare:

1. Se c'è già l'etichetta `AA-Presa in carico`, ci lavora un altro agente: non
   toccarla e scrivilo in un commento.
2. Una issue deve portare la **tua** etichetta (`agente:claude` o
   `agente:codex`); altrimenti non iniziare e scrivilo in un commento.
3. Aggiungi `AA-Presa in carico` e commenta "Presa in carico da <nome
   dell'agente>".
4. Togli l'etichetta quando hai finito, o se ti fermi prima.

```sh
gh api repos/Matleyx78/prova-orchestratore/issues/<numero>/labels -f "labels[]=AA-Presa in carico"
gh api -X DELETE "repos/Matleyx78/prova-orchestratore/issues/<numero>/labels/AA-Presa%20in%20carico"
```

## Lavoro

- Fai solo ciò che chiede la issue, e niente fuori da `src/` e `tests/`.
- Ogni funzione nuova ha almeno un test in `tests/`.
- Prova in locale con `python3 -m unittest discover -s tests -t .`.
- Codice, commenti e messaggi di commit in inglese; pull request in italiano.
- Conventional Commits, con la riga `Assisted-by: <nome dello strumento>`.
- La pull request ha `Closes #N` nella descrizione e indica strumento, modello
  e impegno (se non lo sai, «impegno non noto»).

## Quando fermarsi

1. Apri la pull request e aspetta la CI con **un solo comando che blocca**,
   `scripts/ci-attendi.sh <numero della pull request>`. Tieni l'etichetta.
2. Se un controllo fallisce, correggi sullo stesso ramo, pubblica e aspetta di
   nuovo; dopo tre tentativi fermati e scrivi nella pull request che cosa hai
   visto.
3. Con tutto verde togli l'etichetta, scrivi un riepilogo nella pull request e
   **termina**.

## Passaggio a Claude (solo per Codex)

Se sei Codex, quando hai finito una pull request di lavoro, come **ultima cosa
prima di terminare** scrivi nella pull request **un solo** commento, a
seconda di com'è andata:

- CI verde:

  ```text
  @claude [modello: opus] [impegno: alto] Leggi AGENTS.md e seguilo alla lettera. Rivedi questa pull request come dice AGENTS.md in "Revisione".
  ```

- CI ancora rossa dopo tre tentativi:

  ```text
  @claude [modello: opus] [impegno: alto] Leggi AGENTS.md e seguilo alla lettera. La CI di questa pull request non passa dopo tre tentativi: analizzala come dice AGENTS.md in "Analisi di una CI rossa".
  ```

Non scrivere `@claude` in nessun altro commento: ogni menzione avvia una
sessione di Claude.

Nella pull request e nei commenti scrivi il modello e l'impegno che il
responsabile ti ha indicato nel messaggio di avvio (per esempio «GPT-6.1 Sol,
impegno medio»); se non te li ha indicati, «modello e impegno non noti».

## Revisione

Se ti chiedono di rivedere una pull request che non è tua: prendila in carico,
lascia **un solo commento** che comincia con «Revisione di <nome
dell'agente>», con le segnalazioni numerate (o «Nessuna segnalazione»), togli
l'etichetta e fermati. Non fare commit sulla pull request di un altro.

## Analisi di una CI rossa

Se ti chiedono di analizzare una pull request la cui CI non passa: prendila in
carico, leggi gli errori della CI e il codice, lascia **un solo commento** che
comincia con «Analisi di <nome dell'agente>» con la causa probabile e la
correzione che suggerisci, togli l'etichetta e fermati. Non fare commit.

## Correzioni

Se ti chiedono di correggere la tua pull request dopo una revisione: prendila
in carico, correggi solo ciò che le segnalazioni chiedono, aspetta la CI come
sopra, rispondi con un commento che dice cosa hai corretto, togli l'etichetta e
fermati.
