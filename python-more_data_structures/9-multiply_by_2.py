#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi = a_dictionary.copy()
    for i in multi:
        multi[i] = multi[i] * 2
    return multi
