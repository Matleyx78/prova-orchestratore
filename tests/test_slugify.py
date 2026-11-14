import unittest

from src.slugify import slugify


class SlugifyTest(unittest.TestCase):
    def test_removes_accents_and_punctuation(self) -> None:
        self.assertEqual(slugify("Perché no?"), "perche-no")

    def test_collapses_whitespace_and_trims_hyphens(self) -> None:
        self.assertEqual(slugify("  Ciao   Mondo  "), "ciao-mondo")

    def test_preserves_digits(self) -> None:
        self.assertEqual(slugify("Tappa 0.8 -- PT1"), "tappa-0-8-pt1")

    def test_rejects_an_empty_result(self) -> None:
        with self.assertRaises(ValueError):
            slugify("?!")


if __name__ == "__main__":
    unittest.main()
