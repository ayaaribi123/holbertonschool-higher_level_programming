#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for i in my_string:
        if i != "c":
            s = s + i
        elif i != "C":
            s = s + i
        return s
