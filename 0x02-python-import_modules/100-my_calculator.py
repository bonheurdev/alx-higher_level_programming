#!/usr/bin/python3

if __name__ == "__main__":

    import calculator_1
    import sys

    num_args = len(sys.argv)

    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == '+':
            result = calculator_1.add(a, b)
            print("{} + {} = {}".format(a, b, result))
        elif operator == '-':
            result = calculator_1.sub(a, b)
            print("{} - {} = {}".format(a, b, result))
        elif operator == '*':
            result = calculator_1.mul(a, b)
            print("{} * {} = {}".format(a, b, result))
        elif operator == '/':
            result = calculator_1.div(a, b)
            print("{} / {} = {}".format(a, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
