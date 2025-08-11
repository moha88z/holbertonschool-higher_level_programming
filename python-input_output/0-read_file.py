#!/usr/bin/python3
"""Module that defines a function to read a text file and print its contents."""
def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
