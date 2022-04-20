# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 18:18:52 2021

@author: Brandon
"""

# User inputs 
arrow_base_height = int(input('Enter arrow base height:\n'))
arrow_base_width = int(input('Enter arrow base width:\n'))
arrow_head_width = int(input('Enter arrow head width:\n'))
print()

# Loop to ensure head width is larger than arrow base width
while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))

print()
# Printable line variable in loops
arrow_body = str()
arrow_head = str()

# While loop to set string width and assign to a variable
n=0
while n < arrow_base_width:
        arrow_body = str(arrow_body + '*')
        n += 1

# Print the assigned string "i" number of times based on user input height (number of rows)
i=0
while i < arrow_base_height:
    print(arrow_body)
    i += 1

# Set arrow head starting width based on user input and assign to a variable
a = 0
while a < arrow_head_width:
    arrow_head = str(arrow_head + '*')
    a += 1
    
# Using the same counter variable from the loop above, print diminishing return lines until 0 characters left
# Use [:-1] to truncate the last character of the string
while a > 0:
    print(arrow_head)
    arrow_head = arrow_head[:-1]
    a -=1