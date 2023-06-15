#!/usr/bin/python3
"""a function that returns the weighted average of all integers tuple
(<score>, <weight>)
"""


def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_sum = 0
    total_weight = 0

    for tuple_list in my_list:
        score = tuple_list[0]
        weight = tuple_list[1]

        weighted_value = score * weight
        total_sum += weighted_value
        total_weight += weight

    if total_weight == 0:
        return 0

    weighted_average = total_sum / total_weight
    return weighted_average
