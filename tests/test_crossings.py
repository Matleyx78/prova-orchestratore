import unittest

from src.crossings import count_crossings


class CountCrossingsTest(unittest.TestCase):
    def test_simple_crossing(self) -> None:
        polyline = [(0.0, -1.0), (0.0, 1.0)]

        self.assertEqual(count_crossings(polyline, (-1.0, 0.0), (1.0, 0.0)), 1)

    def test_shared_vertex_counts_once(self) -> None:
        polyline = [(-1.0, 1.0), (0.0, 0.0), (1.0, 1.0)]

        self.assertEqual(count_crossings(polyline, (-1.0, 0.0), (1.0, 0.0)), 1)

    def test_partial_collinear_overlap_counts_once(self) -> None:
        polyline = [(1.0, 0.0), (3.0, 0.0)]

        self.assertEqual(count_crossings(polyline, (0.0, 0.0), (2.0, 0.0)), 1)

    def test_no_contact(self) -> None:
        polyline = [(0.0, 1.0), (2.0, 1.0)]

        self.assertEqual(count_crossings(polyline, (0.0, 0.0), (2.0, 0.0)), 0)


if __name__ == "__main__":
    unittest.main()
