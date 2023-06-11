#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """a function that replaces an element in a list
    a function that replaces an element in a list"""
    list_cpy = my_list[:]
    if idx < 0 or idx > (len(my_list) - 1):
        return list_cpy
    list_cpy[idx] = element
    return list_cpy
