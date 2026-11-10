"""Limit numeric values to an inclusive range."""


def clamp(x: float, lo: float, hi: float) -> float:
    """Return x limited to [lo, hi], rejecting reversed bounds."""
    if lo > hi:
        raise ValueError("Lower bound must not exceed upper bound")
    return min(max(x, lo), hi)
