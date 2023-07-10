#!/usr/bin/python3
"""a function that returns the list of attributes and methods"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    attrs = dir(obj)
    lst = [attr for attr in attrs]
    return lst
