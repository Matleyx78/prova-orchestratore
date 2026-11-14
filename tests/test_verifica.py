"""Run the reference cases in tests/verifica/casi/ against the program.

A case is a JSON file:
    {"funzione": "src.module.name", "argomenti": [...],
     "atteso": value, "tolleranza": 1e-9}            # or
    {"funzione": "...", "argomenti": [...], "errore": "ValueError"}

A case listed in a file of tests/verifica/in-attesa/ is waiting for its work
package and is skipped. The work package removes its lines when it is done.
"""

import builtins
import importlib
import json
import math
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parent / "verifica"


def waiting_cases() -> set:
    names = set()
    for f in (ROOT / "in-attesa").glob("*.txt"):
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                names.add(line.split()[0])
    return names


def load(path: str):
    module_name, _, attr = path.rpartition(".")
    return getattr(importlib.import_module(module_name), attr)


class ReferenceCases(unittest.TestCase):
    def test_cases(self) -> None:
        waiting = waiting_cases()
        for case_file in sorted((ROOT / "casi").glob("*.json")):
            with self.subTest(caso=case_file.name):
                if case_file.name in waiting:
                    self.skipTest(f"{case_file.name} in attesa")
                case = json.loads(case_file.read_text(encoding="utf-8"))
                func = load(case["funzione"])
                args = case.get("argomenti", [])
                if "errore" in case:
                    with self.assertRaises(getattr(builtins, case["errore"])):
                        func(*args)
                    continue
                got = func(*args)
                expected = case["atteso"]
                tol = case.get("tolleranza", 0)
                if isinstance(expected, (int, float)) and tol:
                    self.assertTrue(math.isclose(got, expected, rel_tol=tol, abs_tol=tol),
                                    f"{case_file.name}: atteso {expected}, ottenuto {got}")
                else:
                    self.assertEqual(got, expected, f"{case_file.name}: atteso {expected}, ottenuto {got}")


if __name__ == "__main__":
    unittest.main()
