#!/usr/bin/python3
"""
This module contains code to manipulate squares
"""


class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0) -> None:
        self.__validate_size(size)
        self.__size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__validate_size(size)
        self.__size = size
        return self.__size

    def __validate_size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.size == 0:
            print()
            return
        print((("#" * self.__size) + "\n") * self.__size, end="")
