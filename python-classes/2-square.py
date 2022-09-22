#!/usr/bin/python3
"""class Square that have Private instance attribute size."""


class Square:
    """the Private instance attribute size."""

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
