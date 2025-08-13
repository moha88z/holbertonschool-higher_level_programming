#!/usr/bin/python3
"""Module that converts a JSON string to a Python object"""
import json


def from_json_string(my_str):
    """Return Python object from JSON string"""
    return json.loads(my_str)
