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
        # Parallel or degenerate segments: they meet only when collinear.
        dx, dy = x2 - x1, y2 - y1
        length2 = dx * dx + dy * dy
        if length2 == 0:
            # ab is a single point: it meets cd only if it lies on cd.
            on_line = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3) == 0
            in_box = (min(x3, x4) <= x1 <= max(x3, x4)
                      and min(y3, y4) <= y1 <= max(y3, y4))
            return a if on_line and in_box else None
        if ((x3 - x1) * dy - (y3 - y1) * dx != 0
                or (x4 - x1) * dy - (y4 - y1) * dx != 0):
            return None  # parallel but not on the same line
        tc = ((x3 - x1) * dx + (y3 - y1) * dy) / length2
        td = ((x4 - x1) * dx + (y4 - y1) * dy) / length2
        near, t_near = (c, tc) if tc <= td else (d, td)
        if max(tc, td) < 0 or t_near > 1:
            return None  # collinear but disjoint
        return a if t_near <= 0 else near
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None
