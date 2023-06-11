#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []
    new_list = []
    for elem in my_list:
        if elem % 2 == 0:
            new_list.append(True)
        elif elem % 2 != 0:
            new_list.append(False)
    return new_list
