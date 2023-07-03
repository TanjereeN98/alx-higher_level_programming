#!/usr/bin/python3
def add_integer(a, b=98):
    
    """
    adds up 2 integers only

    Parameters:
    a (int): first parameter
    b (int): second parameter

    Returns:
    int: addition of a + b

    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
