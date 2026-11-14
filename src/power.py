"""Integer exponentiation helper."""


def power(base: float, exp: int) -> float:
    """Return base raised to the integer exponent exp.

    Negative exponents return the reciprocal, so power(2, -2) == 0.25.
    Raises TypeError if exp is not an int and ZeroDivisionError when
    base is zero and exp is negative.
    """
    if isinstance(exp, bool) or not isinstance(exp, int):
        raise TypeError("exp must be an int")
    if exp < 0:
        if base == 0:
            raise ZeroDivisionError("zero cannot be raised to a negative power")
        return 1 / power(base, -exp)
    result = 1
    for _ in range(exp):
        result *= base
    return result
