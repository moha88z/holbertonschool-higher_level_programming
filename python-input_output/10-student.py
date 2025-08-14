#!/usr/bin/python3
"""Defines a Student class with optional JSON attribute filtering."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of the Student instance.
        If attrs is a list of strings, only return those attributes.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
