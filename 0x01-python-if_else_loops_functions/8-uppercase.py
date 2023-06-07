#!/usr/bin/python3
def uppercase(str):
    """
    a function that prints a string in uppercase followed by a new line
    """
    out_str = ""
    for s in str:
        if ord(s) >= 97 and ord(s) < 123:
            out_str += chr(ord(s) - 32)
        else:
            out_str += s
    print(out_str.format())
