#!/usr/bin/python3
"""
This module contains code to check objects
"""


def is_kind_of_class(obj, a_class):
    """
    Returns whether obj is an instance of a_class or any of its children
    """
    return isinstance(obj, a_class)
