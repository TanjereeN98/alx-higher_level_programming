#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """a function that prints a matrix of integers."""
    if matrix is None:
        return
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=" " if j != i[-1] else "")
        print()

