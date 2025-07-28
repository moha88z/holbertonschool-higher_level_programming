#!/usr/bin/python3
"""
This module contains code to manipulate squares
"""


class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0) -> None:
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
