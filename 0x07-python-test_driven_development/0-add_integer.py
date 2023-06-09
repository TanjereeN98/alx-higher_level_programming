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
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
