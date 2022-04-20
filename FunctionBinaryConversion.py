# -*- coding: utf-8 -*-
"""
Base 10 to Binary conversion with a string reversal function included
"""


# This function converts from base 10 to binary but in reverse order
# "reverse_string" function is needed to reverse the order for a valid response
def integer_to_reverse_binary(integer_value):
   digit = int()
   final_number = str()
   while integer_value > 0:
        digit = int(integer_value % 2)
        integer_value = int(integer_value / 2)
        final_number = (str(final_number) + str(digit)) 
   return final_number


# This function reverses the string "HA" returns "AH"
def reverse_string(input_string):
    input_string = ''.join(reversed(input_string))
    return input_string


if __name__ == '__main__':
    integer_value = int(input())

    print(reverse_string(integer_to_reverse_binary(integer_value)))