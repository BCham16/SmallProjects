# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 15:29:04 2021

@author: Brandon
"""

user_list = []
num = 1

while num > 0:
    # Remember to set your input to int variable type
    num = int(input())
    # Add the input number to the list
    user_list.append(num)

# Since last item in the list broke the loop, we need to exclude it from the min/max list
user_list.pop()

# Print the output by converting to strings with a space in between
print(str(min(user_list)) + ' ' + str(max(user_list)))

# This could also be done with sort(user_list) and print the first and last items in the list
