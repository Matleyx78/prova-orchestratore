import math
import unittest

from src.circle import circle_area


class CircleAreaTest(unittest.TestCase):
    def test_positive_radius(self) -> None:
        self.assertEqual(circle_area(2), 4 * math.pi)

    def test_zero_radius(self) -> None:
        self.assertEqual(circle_area(0), 0.0)

    def test_negative_radius(self) -> None:
        with self.assertRaises(ValueError):
            circle_area(-1)


if __name__ == "__main__":
    unittest.main()
