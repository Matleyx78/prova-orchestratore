import unittest

from src.gcd import gcd


class GcdTest(unittest.TestCase):
    def test_positive_integers(self) -> None:
        for a, b, expected in [(48, 18, 6), (18, 48, 6), (7, 13, 1), (12, 12, 12)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(gcd(a, b), expected)

    def test_negative_integers(self) -> None:
        for a, b in [(-48, 18), (48, -18), (-48, -18)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(gcd(a, b), 6)

    def test_one_zero(self) -> None:
        for a, b in [(0, 9), (9, 0), (0, -9), (-9, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(gcd(a, b), 9)

    def test_both_zero(self) -> None:
        self.assertEqual(gcd(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
