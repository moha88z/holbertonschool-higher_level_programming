#!/usr/bin/python3
"""
This module contains classes to manipulate rectangles
"""


class Rectangle:
    """
    This class represents a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        Rectangle.number_of_instances += 1
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
        return ((self.width * f"{self.print_symbol}" + "\n")
                * self.height)[:-1]

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def repr(self):
        return f"Rectangle({self.width}, {self.height})"

    def print(self):
        print(str(self))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(r1, r2):
        if not isinstance(r1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(r2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return r1 if r1.area() >= r2.area() else r2
