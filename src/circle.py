"""Circle formulas."""

import math


def circle_area(r: float) -> float:
    """Return the area of a circle with radius r."""
    if r < 0:
        raise ValueError("radius cannot be negative")
    return math.pi * r**2
