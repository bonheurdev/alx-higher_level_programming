#!/usr/bin/python3
"""computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    var_matrix = [[second ** 2 for second in first] for first in matrix]
    return var_matrix
