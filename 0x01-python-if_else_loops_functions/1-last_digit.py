#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
#  use variable to store {} and .format
var1 = "Last digit of {} is {} and is less than 6 and not 0"
var2 = "Last digit of {} is {} and is less than 6 and not 0"
var3 = "Last digit of {} is {} and is greater than 5"
if (number < 0) and not (last_digit == 0):
    last_digit = -last_digit
    print(f'{var1}'.format(number, last_digit))
elif (last_digit < 6) and not (last_digit == 0):
    print(f'{var2}'.format(number, last_digit))
elif (last_digit > 5):
    print(f'{var3}'.format(number, last_digit))
else:
    print('Last digit of {} is {} and is 0'.format(number, last_digit))
