#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string"""
    ret_str = ""
    for i in my_string:
        if ord(i) != 99 and ord(i) != 67:
            ret_str += i
    return ret_str
