#!/usr/bin/python3
"""containes a class lookup"""


def lookup(obj):
    """retruns a list of  available attributes and methods of an object"""
    return ([x for x in dir(obj)])
