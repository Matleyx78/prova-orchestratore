import unittest

from src.calc import add


class AddTest(unittest.TestCase):
    def test_integers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_floats(self) -> None:
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)


if __name__ == "__main__":
    unittest.main()
