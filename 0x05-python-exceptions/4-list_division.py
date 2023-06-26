#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    idx = 0
    if list_length < idx:
        print("out of range")
    while idx < list_length:
        try:
            res = my_list_1[idx] / my_list_2[idx]
            n_list.append(res)
        except IndexError:
            print("out of range")
            n_list.append(0)
        except TypeError:
            print("wrong type")
            n_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            n_list.append(0)
        finally:
            idx += 1
    return n_list
