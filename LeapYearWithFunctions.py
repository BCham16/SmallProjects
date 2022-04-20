# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:50:31 2021

@author: Brandon
"""

def is_leap_year(user_year):
    # Original code here - works perfect, but project requires a boolean return, not string for 'final_answer' variable
    # if user_year % 100 == 0:
    #     final_answer = 'a leap year' if bool(user_year % 400 == 0) == bool('True') else 'not a leap year'
    # else:
    #     final_answer = 'a leap year' if bool(user_year % 4 == 0) == bool('True') else 'not a leap year'
    # return final_answer
    
    # New code with returning a boolean value instead of a string response
    if user_year % 100 == 0:
        final_answer = bool(user_year % 400 == 0)
    else:
        final_answer = bool(user_year % 4 == 0)
    return final_answer

if __name__ == '__main__':
    user_year = int(input())
    # Original print statement with string returned, but project wanted boolean returned from function
    #print('{} is {}.'.format(user_year, is_leap_year(user_year)))
    print('{} is {}.'.format(user_year, 'a leap year' if is_leap_year(user_year) == bool('True') else 'not a leap year'))