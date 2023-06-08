#!/usr/bin/env python3

if __name__ == "__main__":

    add_0 = __import__('add_0')

    a = 1
    b = 2
    var1 = add_0.add(a, b)

    print("{} + {} = {}".format(a, b, var1))
