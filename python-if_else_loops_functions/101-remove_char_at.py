#!/usr/bin/python3
def remove_char_at(str, n):
    """Creates a copy of str with the character at index n removed."""
    if n < 0:
        return str
    return str[:n] + str[n + 1:]
