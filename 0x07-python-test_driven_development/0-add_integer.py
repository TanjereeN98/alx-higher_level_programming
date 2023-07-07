#!/usr/bin/python3
"""
0-add_integer module
This module tests the add_integer function with mutiple cases
The function takes two arguments, a and b, and returns their sum.
"""


def add_integer(a, b=98):

    """adds up 2 integers only
    Returns: sum of 2 integers
    """
    if a is None:
        raise TypeError("add_integer() missing 1 required argument")
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not (-1e308 < a < 1e308):
        raise TypeError("a must not be infinite or NaN")
    if not (-1e308 < b < 1e308):
        raise TypeError("b must not be infinite or NaN")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
