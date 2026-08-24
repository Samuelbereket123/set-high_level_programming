#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Replicates the behavior of the provided Python bytecode."""
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b) - c
