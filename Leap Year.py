# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:50:31 2021

@author: Brandon
"""

year = int(input())
divisible_by_four = int(0)
divisible_by_four_hundred = int()
final_answer = ''

divisible_by_four = year % 4
divisible_by_four_hundred = year % 400

if year % 100 == 0:
    final_answer = 'leap year' if divisible_by_four_hundred == 0 else 'not a leap year'   
elif divisible_by_four == 0:
    final_answer = 'leap year'
else:
    final_answer = 'not a leap year'
  
print('{} - {}'.format(year, final_answer))