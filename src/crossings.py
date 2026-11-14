"""Utilities for counting intersections with polylines."""

import math

from kernel.geom import segment_intersection

Point = tuple[float, float]


def count_crossings(polyline: list[Point], a: Point, b: Point) -> int:
    """Return the number of distinct places where segment ``ab`` meets a polyline.

    The polyline consists of the closed segments between consecutive points.
    Consequently, an intersection at a shared vertex is counted only once.
    """
    tolerance = 1e-9
    dx, dy = b[0] - a[0], b[1] - a[1]
    length_squared = dx * dx + dy * dy

    def position(point: Point) -> float:
        if length_squared == 0:
            return 0.0
        return ((point[0] - a[0]) * dx + (point[1] - a[1]) * dy) / length_squared

    points: list[float] = []
    overlaps: list[tuple[float, float]] = []
    for start, end in zip(polyline, polyline[1:]):
        near_a = segment_intersection(a, b, start, end)
        if near_a is None:
            continue

        near_b = segment_intersection(b, a, start, end)
        if near_b is not None and not (
            math.isclose(near_a[0], near_b[0], abs_tol=tolerance)
            and math.isclose(near_a[1], near_b[1], abs_tol=tolerance)
        ):
            first, last = sorted((position(near_a), position(near_b)))
            overlaps.append((first, last))
        else:
            points.append(position(near_a))

    merged_overlaps: list[tuple[float, float]] = []
    for first, last in sorted(overlaps):
        if merged_overlaps and first <= merged_overlaps[-1][1] + tolerance:
            previous_first, previous_last = merged_overlaps[-1]
            merged_overlaps[-1] = (previous_first, max(previous_last, last))
        else:
            merged_overlaps.append((first, last))

    distinct_points: list[float] = []
    for point in sorted(points):
        if any(first - tolerance <= point <= last + tolerance
               for first, last in merged_overlaps):
            continue
        if not distinct_points or not math.isclose(
            point, distinct_points[-1], abs_tol=tolerance
        ):
            distinct_points.append(point)

    return len(merged_overlaps) + len(distinct_points)
