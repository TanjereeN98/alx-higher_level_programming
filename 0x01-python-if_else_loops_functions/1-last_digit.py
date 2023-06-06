#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of {:d} is {:d} and is greater than 5"
str2 = "Last digit of {:d} is {:d} and is 0"
str3 = "Last digit of {:d} is {:d} and is less than 6 and not 0"
number_2 = abs(number) % 10
if number_2 > 5:
    print(str1.format(number, number_2))
elif number_2 == 0:
    print(str2.format(number, number_2))
else:
    print(str3.format(number, -number_2))
