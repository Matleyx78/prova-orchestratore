import math
import unittest

from src.sign import sign


class SignTest(unittest.TestCase):
    def test_positive(self) -> None:
        self.assertEqual(sign(3.5), 1)
        self.assertEqual(sign(math.inf), 1)

    def test_negative(self) -> None:
        self.assertEqual(sign(-2), -1)
        self.assertEqual(sign(-math.inf), -1)

    def test_zero(self) -> None:
        self.assertEqual(sign(0), 0)
        self.assertEqual(sign(-0.0), 0)

    def test_returns_int(self) -> None:
        self.assertIs(type(sign(2.0)), int)

    def test_nan(self) -> None:
        with self.assertRaises(ValueError):
            sign(math.nan)


if __name__ == "__main__":
    unittest.main()
