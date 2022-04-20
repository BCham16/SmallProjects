# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 15:57:26 2021

@author: Brandon
"""
# This program takes the first input to set how many additional inputs there are
# It then adds additional inputs to a list, and identifies the lowest value in the list
# Finally it subtracts the lowest value from all integers in the list

# First input = number of integers to enter
count = int(input())
user_list = []

i = 0
while i < count:
    # Input integers
    num = int(input())
    # Add integers to the list
    user_list.append(num)
    i += 1

# Use the last item in the list as the threshold and then remove it from the list    
threshold = min(user_list)


# Print the list with each element on a seperate line
for x in user_list:
    print(x-threshold)