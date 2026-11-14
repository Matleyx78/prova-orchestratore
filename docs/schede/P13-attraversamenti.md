# [P13] `count_crossings`

- **Agente:** codex — **Revisore:** claude
- **File:** `src/crossings.py`, `tests/test_crossings.py`
- **Usa:** `kernel.geom.segment_intersection` (solo il suo contratto)

## Che cosa

`count_crossings(polyline: list[tuple[float, float]], a, b) -> int`: quante volte il segmento `ab` incontra la polilinea (i segmenti tra punti consecutivi). Un punto in comune con la polilinea conta **una** volta anche se cade su un vertice condiviso da due segmenti. Un tratto di `ab` che si sovrappone a un segmento della polilinea, sulla stessa retta, conta **una** volta.

## Prima di scrivere codice

Controlla che il contratto di `segment_intersection` dica che cosa restituisce per due segmenti **sovrapposti sulla stessa retta**: se non lo dice, è un buco del contratto (AGENTS.md, «Buco nel contratto»).

## Test richiesti

- incrocio semplice: 1;
- `ab` passa per un vertice della polilinea: 1;
- `ab` sovrapposto in parte a un segmento della polilinea: 1;
- nessun contatto: 0.
