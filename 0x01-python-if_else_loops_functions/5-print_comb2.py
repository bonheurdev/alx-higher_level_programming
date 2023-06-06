#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:  # Check if it's the last number
        print('{}'.format(i))
    else:
        print('{:02}'.format(i), end=", ")
