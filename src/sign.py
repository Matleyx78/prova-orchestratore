"""Sign of a real number."""

import math


def sign(x: float) -> int:
    """Return -1, 0 or 1 according to the sign of x.

    Raises ValueError if x is NaN.
    """
    if math.isnan(x):
        raise ValueError("sign is undefined for NaN")
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0
