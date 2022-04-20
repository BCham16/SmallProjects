# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 03:31:36 2021

@author: Brandon
"""

# i becomes !
# a becomes @
# m becomes M
# B becomes 8
# o becomes .
# appending "q*s" to the end of the input string


word = input()

password = list(word)
password = [item.replace('a', '@') for item in password]
password = [item.replace('i', '!') for item in password]
password = [item.replace('m', 'M') for item in password]
password = [item.replace('B', '8') for item in password]
password = [item.replace('o', '.') for item in password]
print(''.join(password) + 'q*s')
    