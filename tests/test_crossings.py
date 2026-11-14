import unittest

from src.crossings import count_crossings


class CountCrossingsTest(unittest.TestCase):
    def test_simple_crossing(self) -> None:
        polyline = [(0.0, -1.0), (0.0, 1.0)]

        self.assertEqual(count_crossings(polyline, (-1.0, 0.0), (1.0, 0.0)), 1)

    def test_shared_vertex_counts_once(self) -> None:
        polyline = [(-1.0, 1.0), (0.0, 0.0), (1.0, 1.0)]

        self.assertEqual(count_crossings(polyline, (-1.0, 0.0), (1.0, 0.0)), 1)

    def test_non_integer_shared_vertex_counts_once(self) -> None:
        polyline = [(4.4, -0.1), (-3.7, 0.1), (-4.3, -0.4)]

        self.assertEqual(
            count_crossings(polyline, (-1.0, 0.1), (-4.0, 0.1)), 1
        )

    def test_partial_collinear_overlap_counts_once(self) -> None:
        polyline = [(1.0, 0.0), (3.0, 0.0)]

        self.assertEqual(count_crossings(polyline, (0.0, 0.0), (2.0, 0.0)), 1)

    def test_overlap_ending_at_shared_vertex_is_direction_independent(self) -> None:
        polyline = [(1.0, 0.0), (3.0, 0.0), (3.0, 1.0)]

        self.assertEqual(count_crossings(polyline, (0.0, 0.0), (4.0, 0.0)), 1)
        self.assertEqual(count_crossings(polyline, (4.0, 0.0), (0.0, 0.0)), 1)

    def test_consecutive_overlaps_are_merged_in_both_directions(self) -> None:
        polyline = [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0)]

        self.assertEqual(count_crossings(polyline, (0.5, 0.0), (1.5, 0.0)), 1)
        self.assertEqual(count_crossings(polyline, (1.5, 0.0), (0.5, 0.0)), 1)

    def test_no_contact(self) -> None:
        polyline = [(0.0, 1.0), (2.0, 1.0)]

        self.assertEqual(count_crossings(polyline, (0.0, 0.0), (2.0, 0.0)), 0)


if __name__ == "__main__":
    unittest.main()
