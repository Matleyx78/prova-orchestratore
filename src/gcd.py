"""Greatest common divisor for integers."""


def gcd(a: int, b: int) -> int:
    """Return the nonnegative greatest common divisor of a and b."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
