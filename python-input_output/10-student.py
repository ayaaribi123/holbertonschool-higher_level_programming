#!/usr/bin/python3
"""class"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            new = {}
        for n in attrs:
            if type(n) is not str:
                return self.__dict__
            if n in self.__dict__:
                new[n] = self.__dict__[n]
                return new
