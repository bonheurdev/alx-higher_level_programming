#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        # combine the values of i and j into a two-digit number
        var1 = i * 10 + j
        if var1 == 89:
            print('{:02}'.format(var1))
        elif j > i:
            print('{:02}'.format(var1), end=", ")
