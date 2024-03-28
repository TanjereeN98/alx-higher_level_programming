#!/usr/bin/python3

def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    for i in range(len(list_of_integers)):
        try:
            if list_of_integers[i] >= list_of_integers[i-1]:
                if list_of_integers[i] >= list_of_integers[i+1]:
                    return list_of_integers[i]
            else:
                continue
        except IndexError:
            continue
    return None
