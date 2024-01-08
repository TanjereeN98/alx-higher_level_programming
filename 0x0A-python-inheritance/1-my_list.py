#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """My List Class"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
