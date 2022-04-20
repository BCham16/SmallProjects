# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 01:17:39 2021

@author: Brandon
"""

def is_list_even(my_list):
    n = 0
    for n in my_list:
        if n % 2 != 0:
            return False
    return True

def is_list_odd(my_list):
    n = 0
    for n in my_list:
        if n % 2 == 0:
            return False
    return True


if __name__ == '__main__':
    count = int(input())
    my_list = []
    
    i = 0
    while i < count:
        # Input integers
        num = int(input())
        # Add integers to the list
        my_list.append(num)
        i += 1
    
    print('all even') if (is_list_even(my_list)) == True else 0
    print('all odd') if (is_list_odd(my_list)) == True else 0
    if (is_list_even(my_list)) == False and (is_list_odd(my_list)) == False:
        print('not even or odd')