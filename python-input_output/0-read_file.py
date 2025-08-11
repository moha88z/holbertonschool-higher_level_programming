#!/usr/bin/python3
"""Module that defines a function to read a text file and print its contents."""
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
