#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    var1 = add(a, b)
    print("{} + {} = {}".format(a, b, var1))

    var2 = sub(a, b)
    print("{} - {} = {}".format(a, b, var2))

    var3 = mul(a, b)
    print("{} * {} = {}".format(a, b, var3))

    var4 = div(a, b)
    print("{} / {} = {}".format(a, b, var4))
