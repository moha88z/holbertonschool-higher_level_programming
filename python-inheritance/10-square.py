#!/usr/bin/python3
"""
This module contain a square class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    represent a square
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
