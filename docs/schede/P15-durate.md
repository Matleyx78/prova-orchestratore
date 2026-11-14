# [P15] `parse_duration`

- **Agente:** claude — **Revisore:** codex
- **File:** `src/duration.py`, `tests/test_duration.py`

## Interfaccia

```python
def parse_duration(text: str) -> int:
    """Return the number of minutes in a duration such as "1h30m" or "45m"."""
```

## Che cosa

Il testo deve contenere almeno una componente e deve corrispondere esattamente
a una di queste forme:

- `<ore>h`;
- `<minuti>m`;
- `<ore>h<minuti>m`.

`<ore>` e `<minuti>` sono interi non negativi scritti con una o più cifre
ASCII (`0`–`9`); gli zeri iniziali sono ammessi. Quando la componente dei
minuti segue quella delle ore, il suo valore deve essere compreso tra 0 e 59,
estremi inclusi. La componente dei minuti da sola non ha un limite superiore.

Le componenti, quando sono entrambe presenti, compaiono senza separatori e
nell'ordine ore poi minuti. Ogni stringa che non rispetta esattamente questa
grammatica solleva `ValueError`. I valori che non sono `str` sono fuori dal
contratto.

La funzione restituisce i minuti totali.

## Test richiesti

- `parse_duration("1h30m") == 90`
- `parse_duration("45m") == 45`
- `parse_duration("2h") == 120`
- `parse_duration("0h") == 0`
- `parse_duration("0m") == 0`
- `parse_duration("0h0m") == 0`
- `parse_duration("1h59m") == 119`
- `parse_duration("60m") == 60`
- `parse_duration("001h02m") == 62`
- solleva `ValueError` per ciascuno di `""`, `"30m1h"`, `"1h2h"`,
  `"10m20m"`, `"1h60m"`, `"h"`, `"m"`, `"1"`, `"1x"`, `" 1h"`,
  `"1h "`, `"1 h"`, `"+1h"`, `"-1h"`, `"1.5h"`, `"1h30"`,
  `"1h30m!"` e `"١h"`.
