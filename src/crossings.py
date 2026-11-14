"""Utilities for counting intersections with polylines."""

from kernel.geom import segment_intersection

Point = tuple[float, float]


def count_crossings(polyline: list[Point], a: Point, b: Point) -> int:
    """Return the number of distinct places where segment ``ab`` meets a polyline.

    The polyline consists of the closed segments between consecutive points.
    Consequently, an intersection at a shared vertex is counted only once.
    """
    intersections: set[Point] = set()
    for start, end in zip(polyline, polyline[1:]):
        intersection = segment_intersection(a, b, start, end)
        if intersection is not None:
            intersections.add(intersection)
    return len(intersections)
