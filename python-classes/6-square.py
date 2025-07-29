#!/usr/bin/python3
"""
This module contains code to manipulate squares
"""


class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0, position=(0, 0)) -> None:
        self.__validate_size(size)
        self.__validate_position(position)
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        self.__validate_size(size)
        self.__size = size
        return self.__size

    @position.setter
    def position(self, position):
        self.__validate_position(position)
        self.__position = position
        return self.position

    def __validate_size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.size == 0:
            print()
            return
        print(
            "\n" * self.__position[1]
            + ((" " * self.__position[0] + "#" * self.__size) + "\n")
            * self.__size,
            end="",
        )

    def __validate_position(self, position):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
