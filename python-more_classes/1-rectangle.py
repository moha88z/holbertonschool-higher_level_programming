#!/usr/bin/python3
"""
This module contains classes to manipulate rectangles
"""


class Rectangle:
    """
    This class represents a rectangle
    """

    def __init__(self, width=0, height=0) -> None:
        self.__validate_pos_int(width, "width")
        self.__validate_pos_int(height, "height")
        self.__height = height
        self.__width = width

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
