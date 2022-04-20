# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:50:31 2021

@author: Brandon
"""

year = int(input())
if year % 100 == 0:
    final_answer = 'leap year' if bool(year % 400 == 0) == bool('True') else 'not a leap year'
else:
    final_answer = 'leap year' if bool(year % 4 == 0) == bool('True') else 'not a leap year'
print('{} - {}'.format(year, final_answer))