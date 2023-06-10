#!/usr/bin/python3
"""prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for Row in matrix:
            for Elem in Row:
                print("{:d}".format(Elem), end=" " if Elem != Row[-1] else "")
            print()
