# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 04:00:09 2021

@author: Brandon
"""

user_text = input()

while user_text != 'Quit' and user_text != 'quit' and user_text != 'q':
    print(user_text[::-1])
    user_text = input()