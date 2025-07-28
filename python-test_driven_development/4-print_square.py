#!/usr/bin/python3
"""
Module for printing a square of # characters.
"""


def print_square(size):
    """Prints a square with the character '#'.

    Args:
        size (int): The size (length and width) of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if size == 0:
        return
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print('\n'.join('#' * size for _ in range(size)))
