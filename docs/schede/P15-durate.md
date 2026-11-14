# [P15] `parse_duration`

- **Agente:** claude — **Revisore:** codex
- **File:** `src/duration.py`, `tests/test_duration.py`

## Interfaccia

```python
def parse_duration(text: str) -> int:
    """Return the number of minutes in a duration such as "1h30m" or "45m"."""
```

## Che cosa

Il testo è composto da un numero di ore seguito da `h` e/o da un numero di minuti seguito da `m`, in quest'ordine. Restituisce i minuti totali.

## Test richiesti

- `parse_duration("1h30m") == 90`
- `parse_duration("45m") == 45`
- `parse_duration("2h") == 120`
