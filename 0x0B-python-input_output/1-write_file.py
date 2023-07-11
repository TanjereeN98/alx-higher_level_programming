#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """write a text to the file"""
    with open(filename, 'w', encoding="utf-8") as F:
        return F.write(text)
