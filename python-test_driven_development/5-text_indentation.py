#!/usr/bin/python3
"""
Module that contains the function text_indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Raises TypeError if text is not a string.
    There are no spaces at the beginning or end of each printed line.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in [".", "?", ":"]:
            print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
