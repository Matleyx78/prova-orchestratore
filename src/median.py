"""Utilities for calculating the median of numeric values."""

from collections.abc import Sequence


def median(values: Sequence[float]) -> float:
    """Return the median of values, using the mean for two middle values."""
    if not values:
        raise ValueError("median requires at least one value")

    ordered_values = sorted(values)
    midpoint = len(ordered_values) // 2
    if len(ordered_values) % 2:
        return ordered_values[midpoint]

    return (ordered_values[midpoint - 1] + ordered_values[midpoint]) / 2
