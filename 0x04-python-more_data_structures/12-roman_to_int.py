#!/usr/bin/python3
"""a function  that converts a Roman numeral to an integer"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    Roman_Units = {
        'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
        'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9
    }
    Roman_Tens = {
        'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50,
        'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90
    }
    Roman_Hundr = {
        'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500,
        'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900
    }
    Roman_Thous = {
        'M': 1000, 'MM': 2000, 'MMM': 3000
    }
    result = 0

    for s in roman_string:
        add_result = 0
        string = []
        string.append(s)
        for dictionary in [Roman_Units, Roman_Tens, Roman_Hundr, Roman_Thous]:
            if "".join(string) in dictionary:
                add_result = dictionary["".join(string)]
                break
        result += add_result

    return result
