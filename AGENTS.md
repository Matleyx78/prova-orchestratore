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

- Fai solo ciò che chiede la issue, nei file che il suo tipo permette ("Tipi di
  issue").
- Ogni funzione nuova ha almeno un test in `tests/`.
- Prova in locale con `python3 -m unittest discover -s tests -t .`.
- Codice, commenti e messaggi di commit in inglese; pull request in italiano.
- Conventional Commits, con la riga `Assisted-by: <nome dello strumento>`.
- La pull request ha `Closes #N` nella descrizione e indica strumento, modello
  e impegno (se non lo sai, «impegno non noto»).

## Tipi di issue

Il tipo si riconosce dal titolo e dall'etichetta. La scheda, se c'è, sta in
`docs/schede/` e fa fede.

| Titolo | Etichetta | Che cosa fa l'esecutore | File che può toccare |
|---|---|---|---|
| `[PN]` | `pacchetto` | codice e test | `src/`, `tests/` tranne `tests/verifica/casi/`; può togliere righe dai file di `tests/verifica/in-attesa/` |
| `[RN]` | `riferimenti` | casi di riferimento per un pacchetto | solo `tests/verifica/` |
| `[CN]` | `contratto` | corregge il contratto di `kernel/` secondo la decisione | solo `kernel/` |
| `[IN]` | `revisione-interfacce` | verbale sulle schede, **senza pull request** | nessuno (dopo una decisione: solo `docs/schede/`) |

### Pacchetto (`[PN]`)

- Usa `kernel/` solo per ciò che dicono le sue docstring (il **contratto**), e
  non modificarlo mai. Se ti serve qualcosa che il contratto non dice, è un
  **buco del contratto**: vedi «Buco nel contratto».
- Se la scheda ha casi di riferimento in `tests/verifica/in-attesa/`, togli le
  loro righe: i casi devono passare. Non toccare mai i casi.

### Riferimenti (`[RN]`)

- Scrivi i casi in `tests/verifica/casi/`, un file JSON per caso (formato in
  `tests/test_verifica.py`), ricavando i valori **da calcoli o da fonti
  pubbliche, mai eseguendo il programma**.
- Se la funzione non esiste ancora, elenca i casi in
  `tests/verifica/in-attesa/<RN>.txt`, una riga per caso:
  `<file del caso> #<issue del pacchetto>`.
- Se la funzione esiste già e un tuo caso fallisce, rifai il valore dalle
  fonti. Se le fonti confermano il tuo valore, **può essere un errore del
  programma: non adattare il caso**. Fermati («Fermarsi per una decisione»)
  con il caso, il valore atteso e quello che dà il programma.
- Nella descrizione della pull request scrivi la riga
  `Avvia dopo il merge: #<issue del pacchetto>`: al merge il pacchetto parte
  da solo.

### Buco nel contratto

Se il contratto di `kernel/` non dice ciò che ti serve, non indovinarlo e non
scrivere tu la funzione:

1. apri una issue `[CN] <funzione>: <che cosa manca>` con le etichette
   `contratto` e `decisione` e l'etichetta `agente:` **dell'altro agente**, con
   il problema, le scelte possibili e la riga per riprendere (con il nome
   dell'altro agente, senza chiocciola);
2. sulla tua issue: «Fermarsi per una decisione», con un rimando alla issue del
   contratto; se hai lavoro non pubblicato, pubblica il ramo **senza** pull
   request e scrivi il nome del ramo.

### Contratto (`[CN]`)

Dopo la decisione: una pull request che tocca solo `kernel/`, con in testa alla
descrizione **Revisione del contratto: da fare**, la decisione applicata,
`Closes #<CN>` e `Avvia dopo il merge: #<pacchetto sospeso>`. Poi il passaggio
in revisione. Il revisore scrive come commento il **verbale della revisione del
contratto** con le classi di sempre; un buco nuovo è una [decisione]: non
sceglie lui.

### Revisione delle interfacce (`[IN]`)

Leggi le schede indicate e il contratto che usano. Scrivi nella issue **un
solo** commento «Verbale della revisione delle interfacce», con per ogni scheda
le segnalazioni classificate. Nessuna pull request, nessun commit.

- Almeno una [decisione]: «Fermarsi per una decisione» sulla issue.
- Altrimenti: etichetta `pronta` sulla issue.

Alla ripresa dopo la decisione l'esecutore applica le decisioni alle schede in
**una** pull request che tocca solo `docs/schede/`, con in testa
**Revisione della correzione: da fare** e `Closes #<IN>`, e la passa in
revisione. Il revisore controlla solo le regole nuove o corrette (valgono anche
al contrario? e al limite esatto?) e non sceglie: un buco nuovo è una
[decisione].

## Quando fermarsi

1. Apri la pull request e aspetta la CI con **un solo comando che blocca**,
   `scripts/ci-attendi.sh <numero della pull request>`. Tieni l'etichetta.
2. Se un controllo fallisce, correggi sullo stesso ramo, pubblica e aspetta di
   nuovo; dopo tre tentativi fermati e scrivi nella pull request che cosa hai
   visto.
3. Con tutto verde togli l'etichetta, scrivi un riepilogo nella pull request e
   **termina**, dopo il passaggio in revisione qui sotto.

## Ruoli

Su ogni issue lavorano due agenti:

- l'**esecutore** è quello dell'etichetta `agente:…` della issue: realizza la
  issue e poi corregge;
- il **revisore** è **l'altro** (`claude` se l'esecutore è `codex`, e
  viceversa): rivede, e non fa mai commit sulla pull request.

I passaggi dall'uno all'altro si fanno **solo** con `scripts/passa.sh`, mai
scrivendo a mano `@claude` o `@codex` (nemmeno in un esempio o fra apici): ogni menzione avvia una sessione, e lo
script scrive il testo giusto con l'identità del responsabile, l'unica a cui
gli agenti rispondono.

```sh
scripts/passa.sh <claude|codex> <numero della pull request> revisione <N>
scripts/passa.sh <claude|codex> <numero della pull request> correzioni <N>
scripts/passa.sh <claude|codex> <numero della pull request> analisi
```

Nella pull request e nei commenti scrivi il modello e l'impegno con cui sei
stato avviato; se non li sai, «modello e impegno non noti».

## Passaggio in revisione (esecutore)

Quando hai finito una pull request di lavoro, come **ultima cosa prima di
terminare**:

- CI verde: `scripts/passa.sh <revisore> <numero> revisione 1`;
- CI ancora rossa dopo tre tentativi:
  `scripts/passa.sh <revisore> <numero> analisi`.

## Fermarsi per una decisione

Chiunque tu sia, esecutore o revisore, ti fermi per una decisione quando:

- un caso della issue è sbagliato (per esempio un valore atteso che contraddice
  la descrizione): **non correggerlo e non adattare il codice al caso
  sbagliato**;
- manca un'informazione che né la issue né AGENTS.md danno;
- in revisione, c'è una segnalazione **[decisione]** o si arriva al giro 3 con
  delle [bloccante] ancora aperte.

Allora:

1. aggiungi l'etichetta `decisione` alla issue e, se c'è, alla pull request;
2. scrivi **un solo** commento (nella pull request se c'è, altrimenti nella
   issue) che comincia con «Serve una decisione del responsabile», con il
   problema, le scelte possibili e, come ultima riga, quella da copiare con il
   **tuo** nome, **senza la chiocciola** (una menzione vera avvierebbe subito
   un agente): «Per riprendere scrivi, con @ davanti: `<tuo nome> Decisione
   del responsabile: …`»;
3. se il commento è nella pull request, scrivi nella issue «Serve una decisione
   del responsabile: vedi la pull request #<numero>»;
4. togli `AA-Presa in carico` e termina, senza aspettare la CI.

## Ripresa dopo una decisione

Il responsabile riprende con un commento che comincia con
`@<tuo nome> Decisione del responsabile:`. Prendi in carico, togli `decisione`
dalla issue e dalla pull request, e poi:

- **se eri l'esecutore**: continua il lavoro applicando la decisione, fino al
  passaggio in revisione (o a una nuova decisione);
- **se eri il revisore**: scrivi **un solo** commento che comincia con «Ripresa
  dopo la decisione (giro N)», dove N è il giro che si era fermato (senza
  scrivere «Giro di revisione:»: non è un giro nuovo), con ogni modifica che la
  decisione chiede come **[bloccante]** e le [bloccante] di quel giro ancora
  aperte. Se ce n'è almeno una: `scripts/passa.sh <esecutore> <numero>
  correzioni <N>`; altrimenti aggiungi l'etichetta `pronta`. Togli
  `AA-Presa in carico` e fermati.

## Revisione (revisore)

La richiesta può arrivare nella issue che la pull request chiude: lavori
comunque sulla **pull request** indicata, e lì vanno presa in carico, commento
ed etichette.

Prendi in carico la pull request e lascia **un solo commento** che comincia con
«Revisione di <nome dell'agente>», con la riga «Giro di revisione: N». N è il
numero dei commenti della pull request che contengono «Giro di revisione:», più
uno. Dal giro 2 rivedi **solo i commit di correzione** e le segnalazioni del
giro prima.

Ogni segnalazione comincia con la sua classe:

- **[bloccante]**: la issue non è soddisfatta, un test manca o è sbagliato, una
  regola di AGENTS.md è violata. La risposta è già nella issue o in AGENTS.md;
- **[decisione]**: serve una scelta che né la issue né AGENTS.md fanno;
- **[facoltativa]**: un miglioramento non richiesto.

Alla fine, in quest'ordine:

- almeno una [decisione], o [bloccante] al giro 3 (scrivi «Fermato dopo tre
  giri»): «Fermarsi per una decisione»;
- [bloccante] ai giri 1 o 2: `scripts/passa.sh <esecutore> <numero>
  correzioni <N>`;
- altrimenti (solo [facoltativa] o nessuna segnalazione): etichetta `pronta`.

Poi togli `AA-Presa in carico` e fermati. Non fare commit.

## Analisi di una CI rossa (revisore)

Prendi in carico, leggi gli errori della CI e il codice, lascia **un solo
commento** che comincia con «Analisi di <nome dell'agente>» con la causa
probabile e la correzione che suggerisci, togli l'etichetta e fermati. Non
fare commit.

## Correzioni (esecutore)

Prendi in carico, lavora sul ramo della pull request
(`gh pr checkout <numero>`), correggi solo le **[bloccante]** del giro indicato
e, se c'è, del commento «Ripresa dopo la decisione» di quel giro (le
[facoltativa] e le [decisione] non si toccano). Aspetta la CI come sopra,
rispondi con un commento che dice cosa hai corretto, togli l'etichetta e, come
ultima cosa, `scripts/passa.sh <revisore> <numero> revisione <N+1>`.
