import unittest

from src.lcm import lcm


class LcmTest(unittest.TestCase):
    def test_positive(self) -> None:
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(3, 5), 15)

    def test_one_negative(self) -> None:
        self.assertEqual(lcm(-4, 6), 12)
        self.assertEqual(lcm(4, -6), 12)

    def test_one_zero(self) -> None:
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(7, 0), 0)


if __name__ == "__main__":
    unittest.main()
