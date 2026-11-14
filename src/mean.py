"""Utilities for calculating arithmetic means."""

from collections.abc import Sequence


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of a non-empty numeric sequence."""
    if not values:
        raise ValueError("mean requires at least one value")

    return sum(values) / len(values)
