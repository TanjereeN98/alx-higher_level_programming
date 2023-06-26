#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    i_idx = 0
    while True:
        try:
            if idx < x:
                print("{:d}".format(my_list[idx]), end="")
                i_idx += 1
                idx += 1
            else:
                print()
                return i_idx
        except (ValueError, TypeError):
            idx += 1
