#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for c in matrix:
        for i in c:
            print("{:d}".format(i), end=" ")
        print()
