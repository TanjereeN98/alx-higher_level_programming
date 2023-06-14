#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for elem in matrix:
        new_matrix.append(list(map(lambda n: n ** 2, elem)))
    return new_matrix


