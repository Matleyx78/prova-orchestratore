"""Utilities for turning text into file-name-friendly slugs."""

import re


_ACCENTED_LETTERS = str.maketrans(
    {
        "à": "a",
        "è": "e",
        "é": "e",
        "ì": "i",
        "ò": "o",
        "ù": "u",
    }
)


def slugify(text: str) -> str:
    """Return a lowercase, hyphen-separated slug for *text*.

    Raise ``ValueError`` when the input contains no ASCII letters or digits.
    """
    normalized = text.lower().translate(_ACCENTED_LETTERS)
    slug = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")

    if not slug:
        raise ValueError("text does not contain any letters or digits")

    return slug
