#!/usr/bin/python3
"""a function returns list of available attributes and methods of object"""


def lookup(obj):
    """Returns a list object"""
    return dir(obj)
