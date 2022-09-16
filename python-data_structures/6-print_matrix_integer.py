#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for c in matrix:
        for i in c:
            if c.index(i) != 0:
                print(" ", end="")
            print("{:d}".format(i, c), end="")
        print()
