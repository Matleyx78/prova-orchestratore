import unittest

from src.median import median


class MedianTest(unittest.TestCase):
    def test_odd_number_of_values(self) -> None:
        self.assertEqual(median([7, 1, 3]), 3)

    def test_even_number_of_values(self) -> None:
        self.assertEqual(median([8, 2, 4, 6]), 5)

    def test_empty_sequence(self) -> None:
        with self.assertRaises(ValueError):
            median([])


if __name__ == "__main__":
    unittest.main()
