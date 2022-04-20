# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 02:46:04 2021

@author: Brandon
"""

#base 10 to binary conversion

base_number = int(input('Enter an integer: '))
digit = int()
final_number = str()

while base_number > 0:
    digit = int(base_number % 2)
    base_number = int(base_number / 2)
    final_number = (str(final_number) + str(digit))

print(final_number[::-1])