#!/usr/bin/python3

"""

"""


def add_integer(a=1, b=98):
    """Add two integers
    Returns sum of ints
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    return a + b
