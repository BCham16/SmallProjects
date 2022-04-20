# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 03:02:07 2021

@author: Brandon
"""

phone_number = input()
digit = [int(d) for d in str(phone_number)]

print('({}{}{}) {}{}{}-{}{}{}{}'.format(digit[0], digit[1], digit[2], digit[3], digit[4], digit[5], digit[6], digit[7], digit[8], digit[9]))