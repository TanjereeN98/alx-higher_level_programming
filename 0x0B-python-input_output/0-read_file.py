#!/usr/bin/python
"""read_file function"""


def read_file(filename=""):
    """reading function"""
    with open(filename, 'r', encoding="utf-8") as F:
        print(F.read(), end='')
