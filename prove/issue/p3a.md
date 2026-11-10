etichetta: agente:claude
titolo: [P3a] Funzione divide

Aggiungi `divide(a, b)`, che restituisce `a / b` e con `b == 0` solleva `ZeroDivisionError` con un messaggio chiaro; test anche per l'errore.

**Fatto quando**

- la funzione è in `src/divide.py` e i test in `tests/test_divide.py` (file nuovi:
  non toccare `src/calc.py` né altri file, così le prove non vanno in
  conflitto tra loro);
- la CI della pull request è verde;
- la pull request segue AGENTS.md (presa in carico, `Closes #N`, riepilogo,
  etichetta tolta alla fine).
