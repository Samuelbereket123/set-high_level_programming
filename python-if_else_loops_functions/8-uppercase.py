#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    for c in str:
        code = ord(c)
        if 97 <= code <= 122:
            c = chr(code - 32)
        print("{}".format(c), end="")
    print("")
