"""Geometry kernel used by the packages (stands for solid-space).

The docstrings of this module are the **contract**: packages rely only on what
they state. Changing them needs a contract issue and a contract pull request
(AGENTS.md, "Contratto").
"""

from typing import Optional, Tuple

Point = Tuple[float, float]


def segment_intersection(a: Point, b: Point, c: Point, d: Point) -> Optional[Point]:
    """Return the intersection point of segment ab with segment cd.

    Returns ``None`` when the segments do not meet. Segments are closed: their
    end points belong to them. When the segments are collinear and overlap,
    returns the end point of the overlapping part nearest to ``a``.
    """
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = a, b, c, d
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0:
        return _collinear_overlap(a, b, c, d)
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None


def _collinear_overlap(a: Point, b: Point, c: Point, d: Point) -> Optional[Point]:
    """Return the end of the overlap of parallel segments ab and cd nearest to a."""
    (x1, y1), (x2, y2) = a, b
    dx, dy = x2 - x1, y2 - y1
    length2 = dx * dx + dy * dy
    if length2 == 0:
        # ab is a single point: it overlaps cd only if it lies on cd.
        return a if _on_segment(a, c, d) else None
    if (c[0] - x1) * dy - (c[1] - y1) * dx != 0:
        return None  # parallel but not on the same line
    if (d[0] - x1) * dy - (d[1] - y1) * dx != 0:
        return None
    tc = ((c[0] - x1) * dx + (c[1] - y1) * dy) / length2
    td = ((d[0] - x1) * dx + (d[1] - y1) * dy) / length2
    near, t_near = (c, tc) if tc <= td else (d, td)
    t_far = max(tc, td)
    if t_far < 0 or t_near > 1:
        return None
    return a if t_near <= 0 else near


def _on_segment(p: Point, c: Point, d: Point) -> bool:
    """Tell whether point p lies on the closed segment cd."""
    if (d[0] - c[0]) * (p[1] - c[1]) - (d[1] - c[1]) * (p[0] - c[0]) != 0:
        return False
    return (min(c[0], d[0]) <= p[0] <= max(c[0], d[0])
            and min(c[1], d[1]) <= p[1] <= max(c[1], d[1]))
