#!/usr/bin/python3
"""class rectangle that defines a rectangle"""


class Rectangle():
    """empty class rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        str = ""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            for i in range(self.__height):
                for c in range(self.__width):
                    str = str + "#"
                if i <= self.__height - 1:
                    str = str + "\n"
            return str
