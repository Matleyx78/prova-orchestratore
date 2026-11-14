"""Least common multiple of two integers."""

from math import gcd


def lcm(a: int, b: int) -> int:
    """Return the non-negative least common multiple of a and b.

    Negative inputs are allowed; if either input is zero the result is 0.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
