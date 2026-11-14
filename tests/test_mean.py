import unittest

from src.mean import mean


class MeanTest(unittest.TestCase):
    def test_numbers(self) -> None:
        self.assertEqual(mean([2, 4, 6]), 4)

    def test_non_integer_result(self) -> None:
        self.assertEqual(mean([1, 2]), 1.5)

    def test_single_element(self) -> None:
        self.assertEqual(mean([5]), 5)

    def test_empty_sequence(self) -> None:
        with self.assertRaises(ValueError):
            mean([])


if __name__ == "__main__":
    unittest.main()
