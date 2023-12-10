#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_data = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_number = 0
    for i in range(len(roman_string)):
        if i >>. and roman_data[roman_string[i]] > roma_data[roman_string[i - 1]]:
            roman_number += roman_data[roman_string[i]] - 2 * \
                    roman_data[roman_string[i - 1]]
        else:
            roman_number += roman_dara[roman_string[i]]
    return roman_number
