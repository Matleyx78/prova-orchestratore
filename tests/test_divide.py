import unittest

from src.divide import divide


class DivideTest(unittest.TestCase):
    def test_integers(self) -> None:
        self.assertEqual(divide(6, 3), 2)

    def test_floats(self) -> None:
        self.assertAlmostEqual(divide(1, 4), 0.25)
        self.assertAlmostEqual(divide(1.5, 0.5), 3.0)

    def test_negative(self) -> None:
        self.assertEqual(divide(-9, 3), -3)

    def test_zero_divisor_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError) as ctx:
            divide(5, 0)
        self.assertEqual(str(ctx.exception), "cannot divide 5 by zero")

    def test_float_zero_divisor_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError) as ctx:
            divide(5, 0.0)
        self.assertEqual(str(ctx.exception), "cannot divide 5 by zero")


if __name__ == "__main__":
    unittest.main()
