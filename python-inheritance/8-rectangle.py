#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""class Rectangle"""
class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.height = height
