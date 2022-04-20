# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 02:55:43 2021

@author: Brandon
"""

# Get user input, unknown number of elements seperated by space
user_input = input()

# split the string gathered above and define the list they will be added to    
individuals = user_input.split()
data_list = []

# add elements from the input string that has been split to a list
for x in individuals:
    data_list.append(int(x))

sum_inputs = 0
max_number = 0

# cycle through items in the list, sum them, and test / record the largest number
for i in data_list:
    sum_inputs += int(i)
    max_number = i if i > max_number else max_number

print('{:.0f} {}'.format((int(sum_inputs) / (len(data_list))), max_number))



    
    