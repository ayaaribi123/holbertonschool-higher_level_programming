#!/usr/bin/python3
"""class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        self.width = size
        self.height = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """update"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.size = args[1]
            if i == 2:
                self.x = args[2]
            if i == 3:
                self.y = args[3]
        else:
            for i in kwargs.keys():
                if i == "id":
                    self.id = kwargs["id"]
                if i == "size":
                    self.width = kwargs["size"]
                if i == "x":
                    self.x = kwargs["x"]
                if i == "y":
                    self.y = kwargs["y"]
