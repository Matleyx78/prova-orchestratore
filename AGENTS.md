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

Dal secondo giro rivedi **solo i commit di correzione** e le segnalazioni del
giro prima. Non scrivere mai `@codex` né `@claude` nel testo della revisione.

### Giri di revisione (solo per Claude, sulle pull request di Codex)

1. **Numero del giro.** Conta i commenti della pull request che contengono
   «Giro di revisione:». Il tuo giro è quel numero più uno; scrivi nella
   revisione la riga «Giro di revisione: N».
2. **Classifica ogni segnalazione** con una di queste etichette all'inizio:
   - **[bloccante]**: la issue non è soddisfatta, un test manca o è sbagliato,
     una regola di AGENTS.md è violata. Si corregge senza chiedere niente al
     responsabile, perché la risposta è già nella issue o in AGENTS.md;
   - **[decisione]**: serve una scelta che né la issue né AGENTS.md fanno (per
     esempio cambiare il comportamento richiesto);
   - **[facoltativa]**: un miglioramento non richiesto.
3. **Alla fine della revisione**, in quest'ordine:
   - se c'è almeno una **[decisione]**: aggiungi l'etichetta `decisione` alla
     pull request **e alla issue che chiude** (quella di `Closes #N`), scrivi
     nella issue «Serve una decisione del responsabile: vedi la pull request
     #<numero>» e non passare niente a Codex;
   - altrimenti, se ci sono **[bloccante]** e il giro è 1 o 2: lancia
     `scripts/passa-a-codex.sh <numero della pull request> <N>`;
   - altrimenti, se ci sono **[bloccante]** al giro 3: aggiungi l'etichetta
     `decisione` alla pull request e alla issue, come sopra, e scrivi nella
     revisione «Fermato dopo tre giri»;
   - altrimenti (solo **[facoltativa]** o nessuna segnalazione): aggiungi
     l'etichetta `pronta`.

### Ripresa dopo una decisione (solo per Claude)

Il responsabile riprende una pull request ferma con un commento che comincia
con `@claude Decisione del responsabile:`. Allora:

1. Prendi in carico e togli l'etichetta `decisione` dalla pull request e dalla
   issue che chiude.
2. Scrivi **un solo** commento che comincia con «Ripresa dopo la decisione
   (giro N)», dove N è il giro della revisione che si era fermata. Non
   scriverci «Giro di revisione:»: la ripresa non è un giro nuovo. Elenca:
   - ogni modifica che la decisione chiede, come **[bloccante]**;
   - le **[bloccante]** di quel giro ancora aperte.
3. Poi:
   - se l'elenco ha almeno una [bloccante]: lancia
     `scripts/passa-a-codex.sh <numero della pull request> <N>`;
   - altrimenti: aggiungi l'etichetta `pronta`.
4. Togli `AA-Presa in carico` e fermati. Non fare commit.

Se la decisione lascia aperta un'altra scelta, rimetti `decisione` come al
punto 3 dei giri.

## Analisi di una CI rossa

Se ti chiedono di analizzare una pull request la cui CI non passa: prendila in
carico, leggi gli errori della CI e il codice, lascia **un solo commento** che
comincia con «Analisi di <nome dell'agente>» con la causa probabile e la
correzione che suggerisci, togli l'etichetta e fermati. Non fare commit.

## Correzioni

Se ti chiedono di correggere la tua pull request dopo una revisione: prendila
in carico, correggi solo le segnalazioni **[bloccante]** del giro indicato e,
se c'è, del commento «Ripresa dopo la decisione» di quel giro (le
[facoltativa] e le [decisione] non si toccano), aspetta la CI come sopra,
rispondi con un commento che dice cosa hai corretto, togli l'etichetta e
fermati. Lavori sul ramo della pull request: `gh pr checkout <numero>`.

Se sei Codex, come ultima cosa scrivi **un solo** commento per il giro dopo,
mettendo al posto di «N+1» il giro che ti hanno indicato più uno:

```text
@claude [modello: opus] [impegno: alto] Leggi AGENTS.md e seguilo alla lettera. Rivedi i commit di correzione di questa pull request come dice AGENTS.md in "Revisione" (giro N+1).
```
