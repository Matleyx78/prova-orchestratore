import unittest

from src.clamp import clamp


class ClampTest(unittest.TestCase):
    def test_value_inside_range(self) -> None:
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_value_below_range(self) -> None:
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_value_above_range(self) -> None:
        self.assertEqual(clamp(12, 0, 10), 10)

    def test_inclusive_bounds(self) -> None:
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_equal_bounds(self) -> None:
        self.assertEqual(clamp(3, 2, 2), 2)

    def test_float_values(self) -> None:
        self.assertEqual(clamp(-1.5, -1.0, 0.5), -1.0)
        self.assertEqual(clamp(0.25, -1.0, 0.5), 0.25)

    def test_reversed_bounds(self) -> None:
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)


if __name__ == "__main__":
    unittest.main()
