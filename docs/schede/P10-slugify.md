# [P10] `slugify`

- **Agente:** codex — **Revisore:** claude
- **File:** `src/slugify.py`, `tests/test_slugify.py`

## Che cosa

`slugify(text: str) -> str` trasforma un testo in una forma adatta a un nome di file:

1. lettere minuscole;
2. lettere accentate senza accento (`à è é ì ò ù` → `a e e i o u`);
3. ogni gruppo di caratteri che non sono lettere `a`–`z` o cifre diventa **un solo** trattino;
4. niente trattini all'inizio e alla fine;
5. se il risultato è vuoto, solleva `ValueError`.

## Test richiesti

- `slugify("Perché no?") == "perche-no"`
- `slugify("  Ciao   Mondo  ") == "ciao-mondo"`
- `slugify("Tappa 0.8 -- PT1") == "tappa-0-8-pt1"`
- `slugify("?!") ` solleva `ValueError`
