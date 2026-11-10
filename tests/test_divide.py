import unittest

from src.divide import divide


class DivideTest(unittest.TestCase):
    def test_integers(self) -> None:
        self.assertEqual(divide(6, 3), 2)

    def test_floats(self) -> None:
        self.assertAlmostEqual(divide(1, 4), 0.25)

    def test_negative(self) -> None:
        self.assertEqual(divide(-9, 3), -3)

    def test_zero_divisor_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError) as ctx:
            divide(5, 0)
        self.assertIn("by zero", str(ctx.exception))

    def test_float_zero_divisor_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0.0)


if __name__ == "__main__":
    unittest.main()
