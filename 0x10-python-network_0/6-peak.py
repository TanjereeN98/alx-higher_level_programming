#!/usr/bin/python3
"""function that finds a peak of the array"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if list_of_integers:
        lf = 0
        r = len(list_of_integers) - 1
        while lf < r:
            m = (r + lf) // 2
            if list_of_integers[m] > list_of_integers[m + 1]:
                r = m
            else:
                lf = m + 1
        return list_of_integers[lf]
