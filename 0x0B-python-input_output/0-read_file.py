#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """read the file and print its content to the stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
