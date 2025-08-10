#!/usr/bin/python3
"""this Module is about learning abc class """
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    an abstract class that does a thing
    """

    @abstractmethod
    def area(self):
        """a function"""
        pass

    @abstractmethod
    def perimeter(self):
        """a function"""
        pass


class Circle(Shape):
    """
    a circle class that inherits from shape
    """

    def __init__(self, radius):
        """a function"""
        self.radius = abs(radius)

    def area(self):
        """a function"""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """a function"""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    a Rectangle class that inherits from shape
    """

    def __init__(self, width, height):
        """a function"""
        self.width = width
        self.height = height

    def area(self):
        """a function"""
        return self.width * self.height

    def perimeter(self):
        """a function"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """a function"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
