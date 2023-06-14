#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for elem in set(my_list):
        res += elem
    return res
