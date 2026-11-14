import unittest

from src.percent import percent


class PercentTest(unittest.TestCase):
    def test_half_is_fifty_percent(self) -> None:
        self.assertEqual(percent(1, 2), 50.0)

    def test_quarter_is_twenty_five_percent(self) -> None:
        self.assertEqual(percent(1, 4), 25.0)

    def test_whole_is_one_hundred_percent(self) -> None:
        self.assertEqual(percent(3, 3), 100.0)

    def test_zero_whole_raises_zero_division_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            percent(1, 0)


if __name__ == "__main__":
    unittest.main()
