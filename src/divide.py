"""Division helper."""


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises ZeroDivisionError with a clear message when b is zero.
    """
    if b == 0:
        raise ZeroDivisionError(f"cannot divide {a} by zero")
    return a / b
