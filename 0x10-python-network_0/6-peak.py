#!/usr/bin/python3
"""function that finds a peak of the array"""


def find_peak(list_of_integers):
    """find a peak"""
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    for i in range(len(list_of_integers)):
        try:
            if list_of_integers[i - 1] <= list_of_integers[i]:
                if list_of_integers[i + 1] <= list_of_integers[i]:
                    return list_of_integers[i]
        except IndexError:
            try:
                if list_of_integers[i] >= list_of_integers[i+1]:
                    return list_of_integers[i]
            except IndexError:
                if list_of_integers[i] > list_of_integers[i - 1]:
                    return list_of_integers[i]
    return None