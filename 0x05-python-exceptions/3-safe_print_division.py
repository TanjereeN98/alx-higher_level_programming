#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except Exception:
        res = None
    finally:
        if res is not None:
            print("Inside result: {:.1f}".format(res))
        else:
            print("Inside result: {}".format(res))
        return res
