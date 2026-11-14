import unittest

from src.power import power


class PowerTest(unittest.TestCase):
    def test_positive_exponent(self) -> None:
        self.assertEqual(power(2, 3), 8)

    def test_zero_exponent(self) -> None:
        self.assertEqual(power(5, 0), 1)

    def test_negative_exponent(self) -> None:
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_negative_base(self) -> None:
        self.assertEqual(power(-3, 3), -27)

    def test_zero_base_negative_exponent(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)

    def test_non_integer_exponent(self) -> None:
        with self.assertRaises(TypeError):
            power(2, 1.5)


if __name__ == "__main__":
    unittest.main()
