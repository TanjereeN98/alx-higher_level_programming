#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, div, mul
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+':
        a = add(int(argv[1]), int(argv[3]))
        print("{} + {} = {}".format(argv[1], argv[3], a))
    elif argv[2] == '-':
        s = sub(int(argv[1]), int(argv[3]))
        print("{} - {} = {}".format(argv[1], argv[3], s))
    elif argv[2] == '*':
        m = mul(int(argv[1]), int(argv[3]))
        print("{} * {} = {}".format(argv[1], argv[3], m))
    elif argv[2] == '/':
        d = div(int(argv[1]), int(argv[3]))
        print("{} / {} = {}".format(argv[1], argv[3], d))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
