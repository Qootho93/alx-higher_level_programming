#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for idx, row in enumerate(new_matrix):
        for idx1, col in enumarate(new_matrix):
            new_matrix[idx1] = row[idx1] ** 2
    return new_matrix
