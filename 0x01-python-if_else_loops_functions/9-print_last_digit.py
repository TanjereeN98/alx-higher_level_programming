#!/usr/bin/python3
def print_last_digit(number):
    """
    print last digit of a number
    """
    print(number, end="")
    return abs(number) % 10
