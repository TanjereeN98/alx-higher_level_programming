#!/usr/bin/python3


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix"""
    if (not isinstance(matrix, list)
        or not all(isinstance(lst, list) for lst in matrix)
        or not all(isinstance(item, int) or isinstance(item, float)
                   for lst in matrix for item in lst)):
        message = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(message)
    if not all(len(matrix[0]) == len(lst) for lst in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), lst)) for lst in matrix])
