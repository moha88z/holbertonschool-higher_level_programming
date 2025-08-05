#!/usr/bin/python3
"""
This module check objects
"""


def inherits_from(obj, a_class):
    """
    Return true if obj is instance from any of a_class children
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
