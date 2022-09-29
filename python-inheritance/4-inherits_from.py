#!/usr/bin/python3
"""check if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """check if the object an instance of a class that inherited"""
    if type(obj) == a_class:
        return False
    else:
    	return isinstance(obj, a_class)
