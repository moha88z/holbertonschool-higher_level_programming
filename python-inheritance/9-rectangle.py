#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""

baseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that defines a rectangle using BaseGeometry"""
    def __inti__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

def area(self):
    return self._width * slef.__height

def __str__(self):
    return "[Rectangle] {}/{}".format(self.__width, slef.__height)
        
