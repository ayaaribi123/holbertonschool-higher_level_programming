#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
if number < 0:
    number = number % 10
if number == 0:
    print("last digit of", number, "is", last_digit, "and is 0")
if number > 5:
    print("last digit", number, "is", last_digit, "and is greater than 5")
else:
    print("last digit of", number, "is", last_digit, "and is less than 6 and not 0")
