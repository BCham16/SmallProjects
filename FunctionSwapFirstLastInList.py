# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 04:06:16 2021

@author: Brandon
"""

# This is a simple function to swap the first and last items in a list

def swap(values_list):
    first_item = values_list[0]
    last_item = values_list[-1]
    values_list[-1] = first_item
    values_list[0] = last_item
      
    
values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)