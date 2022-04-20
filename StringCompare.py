# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 03:00:29 2021

@author: Brandon
"""

# This program takes 2 inputs for a "simon says" game
# simon_pattern input is the simon says pattern
# user_pattern input is the user attempting to copy simon
# The for loop checks each character of both strings and assigns a point for each match
# The for loop breaks when a mismatch is found

user_score = 0
simon_pattern = input()
user_pattern  = input()

index = 0
for character in simon_pattern:
    #print(character + '=' + user_pattern[index])
    if user_pattern[index] == character:
        user_score += 1
    else:
        break
    index += 1

print('User score:', user_score)