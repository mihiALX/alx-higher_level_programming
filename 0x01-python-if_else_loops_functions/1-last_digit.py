#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = " and is greater than 5"
str2 = " and is 0"
str3 = " and is less than 6 and not 0"
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    print(f"Last digit of {number} is {last}" + str1)
elif last == 0:
    print(f"Last digit of {number} is {last}" + str2)
else:
    print(f"Last digit of {number} is {last}" + str3)
