import unittest

from src.multiply import multiply


class MultiplyTest(unittest.TestCase):
    def test_integers(self) -> None:
        self.assertEqual(multiply(2, 3), 6)

    def test_negative_and_zero(self) -> None:
        self.assertEqual(multiply(-4, 5), -20)
        self.assertEqual(multiply(7, 0), 0)

    def test_floats(self) -> None:
        self.assertAlmostEqual(multiply(0.5, 0.2), 0.1)


if __name__ == "__main__":
    unittest.main()
