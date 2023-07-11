#!/usr/bin/python
"""Re a function that reads a text file (UTF8)
    and prints it to stdout:
"""


def read_file(filename=""):
    """reading function"""
    with open(str(filename), encoding="utf-8") as F:
        print(F.read(), end='')
