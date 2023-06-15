#!/usr/bin/python3
"""a function  that converts a Roman numeral to an integer"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
        'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
        'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50,
        'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90,
        'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500,
        'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900,
        'M': 1000, 'MM': 2000, 'MMM': 3000
    }

    result = 0

    while roman_string:
        for numeral in sorted(roman_numerals, key=len, reverse=True):
            if roman_string.startswith(numeral):
                result += roman_numerals[numeral]
                roman_string = roman_string[len(numeral):]
                break
        else:
            return 0

    return result
