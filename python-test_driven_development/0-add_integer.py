#!/usr/bin/python3
"""
Module that defines an integer addition function.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    a and b are casted to integers if they are floats.
    Raises TypeError if neither is an int or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
