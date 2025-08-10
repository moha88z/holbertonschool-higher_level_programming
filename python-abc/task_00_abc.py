#!/usr/bin/env python3
"""this Module is about learning abc class """


from abc import ABC, abstractmethod


class Animal(ABC):
    """an abstract class"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """a class inherits from an abstract class"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """a class inherits from an abstract class"""

    def sound(self):
        return "Meow"
