#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not integer.
        ValueError: If size is less then 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for row in range(size):
        print("#" * size)
