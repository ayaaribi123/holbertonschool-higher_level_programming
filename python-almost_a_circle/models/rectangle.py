#!/usr/bin/python3
"""class rectangle"""

from models.base import Base


class Rectangle(Base):

    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        id = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area
        """
        return self.__width * self.__height

    def display(self):
        """dispaly"""
        for i in range(self.__height):
            for c in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def display(self):
        """display"""
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for c in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.width = args[1]
            if i == 2:
                self.height = args[2]
            if i == 3:
                self.x = args[3]
            if i == 4:
                self.y = args[4]
        else:
            for i in kwargs.keys():
                if i == "id":
                    self.id = kwargs["id"]
                if i == "width":
                    self.width = kwargs["width"]
                if i == "height":
                    self.height = kwargs["height"]
                if i == "x":
                    self.x = kwargs["x"]
                if i == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """to dictionary"""
        return {"x": self.x, "y": self.y,
                "id": self.id, "height": self.height, "width": self.width}
