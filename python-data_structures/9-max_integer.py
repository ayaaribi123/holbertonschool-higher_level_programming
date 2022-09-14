#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = my_list[0]
    for c in my_list:
        if c > i:
            i = c
    return i