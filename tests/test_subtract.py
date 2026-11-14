import unittest

from src.subtract import subtract


class SubtractTest(unittest.TestCase):
    def test_integers(self) -> None:
        self.assertEqual(subtract(7, 3), 4)

    def test_negative_result(self) -> None:
        self.assertEqual(subtract(3, 7), -4)

    def test_floats(self) -> None:
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)

    def test_negative_operands(self) -> None:
        self.assertEqual(subtract(-2, -5), 3)

    def test_zero_operand(self) -> None:
        self.assertEqual(subtract(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
