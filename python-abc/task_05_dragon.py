#!/usr/bin/python3
"""this Module is about learning abc class """


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon (FlyMixin, SwimMixin):
    def roar(self):
        print("The dragon roars!")
