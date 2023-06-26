#!/usr/bin/python3
"""error handling using try and except in the safe_print_list function"""


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for index in range(x):
            print(my_list[index], end='')
            count += 1
    except IndexError:
        pass

    print()
    return count
