#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for elem in matrix:
        new_matrix.append(list(map(lambda x: x * x, elem)))
    return new_matrix


