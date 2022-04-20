# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 15:57:26 2021

@author: Brandon
"""
# This program takes the first input to set how many additional inputs there are
# It then adds additional inputs to a list, but saves the last integer as a threshold
# Finally it removes any items from the list that are above the set threshold

def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):

    # Redefine the list with only elements below the defined threshold
    user_values = [n for n in user_values if n <= upper_threshold]
    
    # Print the list with each element on a seperate line
    for x in user_values:
        print(x)

def get_user_values():
    # First input = number of integers to enter
    count = int(input())
    user_values = []
    
    i = 0
    while i < count:
        # Input integers
        num = int(input())
        # Add integers to the list
        user_values.append(num)
        i += 1
    
    # Use the last item in the list as the threshold and then remove it from the list    
    upper_threshold = user_values[-1]
    del user_values[-1]
    
    return user_values, upper_threshold


if __name__ == '__main__':

    user_values, upper_threshold = get_user_values()
    output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)