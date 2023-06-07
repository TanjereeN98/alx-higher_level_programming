#!/usr/bin/python3
def uppercase(str):
    """
    a function that prints a string in uppercase followed by a new line
    """
    print_str = ""
    for s in str:
        if ord(s) >= 97 and ord(s) < 123:
            print_str += chr(ord(s) - 32)
        else:
            print_str += s
    print(print_str.format())
