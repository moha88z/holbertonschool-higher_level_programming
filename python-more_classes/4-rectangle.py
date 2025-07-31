#!/usr/bin/python3
"""
This module contains classes to manipulate rectangles
"""


class Rectangle:
    """
    This class represents a rectangle
    """

    def __init__(self, width=0, height=0) -> None:
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, v):
        self.__validate_pos_int(v, "width")
        self.__width = v
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, v):
        self.__validate_pos_int(v, "height")
        self.__height = v
        return self.__height

    def __validate_pos_int(self, value, name):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        if self.width == 0:
            return ""
        return ((self.width * "#" + "\n") * self.height)[:-1]

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def repr(self):
        return f"Rectangle({self.width}, {self.height})"

    def print(self):
        print(str(self))
