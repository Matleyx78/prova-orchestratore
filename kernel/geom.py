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
    end points belong to them.
    """
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = a, b, c, d
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None
