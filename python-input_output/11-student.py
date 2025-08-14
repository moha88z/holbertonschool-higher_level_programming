#!/usr/bin/python3
"""Defines a Student class with JSON serialization and deserialization."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dict representation of the Student instance.

        If attrs is a list of strings, only those attribute names present
        on the instance are returned.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        with those from the given dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
