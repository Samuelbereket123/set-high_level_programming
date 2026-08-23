#!/usr/bin/python3
"""
Module that contains the function print_square.
"""


def print_square(size):
    """
    Prints a square with the character # of a given size.

    Raises TypeError if size is not an integer.
    Raises ValueError if size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
