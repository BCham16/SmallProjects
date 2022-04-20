# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 03:17:11 2021

@author: Brandon
"""

first_num = int(input())
second_num = int(input())

step = first_num
final = []

if second_num < first_num:
    print("Second integer can't be less than the first.")
    quit()

while step <= second_num:
    final.append(step)
    step += 10

#print final list as a string with spaces using for loop    
for i in final:
    print(i, end=' ')

# alternative way to join the list into one string
#final = ' '.join(map(str, final))
#print(final)