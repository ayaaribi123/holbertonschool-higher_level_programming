#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
less = "and is less than 6 and not 0"
if number < 0:
    number = (number * -1) % 10
if number == 0:
    print("Last digit of", number, "is", number, "and is 0")
if number > 5:
    print("Last digit of", number, "is", number, "and is greater than 5")
else:
    print("Last digit of", number, "is", number, less)
