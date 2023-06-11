#!/usr/bin/python3
"""finds the biggest integer of a list"""


def max_integer(my_list=[]):
    if my_list:
        if len(my_list) == 0:
            return None
        else:
            MAX = my_list[0]
            var1 = my_list[0]
            for num in my_list[1:]:
                if num >= var1:
                    var1 = num
            MAX = var1
            return MAX
