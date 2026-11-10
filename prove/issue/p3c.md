etichetta: agente:codex
titolo: [P3c] Funzione mean

Aggiungi `mean(values)`, media di una sequenza di numeri; con sequenza vuota solleva `ValueError`; test anche per l'errore.

**Fatto quando**

- la funzione è in `src/mean.py` e i test in `tests/test_mean.py` (file nuovi:
  non toccare `src/calc.py` né altri file, così le prove non vanno in
  conflitto tra loro);
- la CI della pull request è verde;
- la pull request segue AGENTS.md (presa in carico, `Closes #N`, riepilogo,
  etichetta tolta alla fine).
