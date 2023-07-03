#!/usr/bin/python3
"""
Contains the definition of 'matrix_divided' function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A matrix of integers or floats.
        div (int or float): The divisor of all elements.

    Returns:
        list: A new matrix.

    Raises:
        TypeError:
                If the divisor is not a number.
                If one row not the same size as other rows.
                If the matrix contains element not integer nor float.
        ZeroDivisionError: If the divisor is equal to 0
    """
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(
            isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(val/div, 2) for val in row] for row in matrix]
