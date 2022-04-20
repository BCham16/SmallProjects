# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 03:50:31 2021

@author: Brandon
"""


def miles_to_laps(user_miles):
    num_laps = user_miles * 4
    return num_laps


if __name__ == '__main__':
    user_miles = float(input())
    num_laps = 0
    print('{:.2f}'.format(miles_to_laps(user_miles)))
    