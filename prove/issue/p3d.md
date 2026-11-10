etichetta: agente:codex
titolo: [P3d] Funzione clamp

Aggiungi `clamp(x, lo, hi)`, che limita `x` tra `lo` e `hi`; con `lo > hi` solleva `ValueError`; almeno tre test.

**Fatto quando**

- la funzione è in `src/clamp.py` e i test in `tests/test_clamp.py` (file nuovi:
  non toccare `src/calc.py` né altri file, così le prove non vanno in
  conflitto tra loro);
- la CI della pull request è verde;
- la pull request segue AGENTS.md (presa in carico, `Closes #N`, riepilogo,
  etichetta tolta alla fine).
