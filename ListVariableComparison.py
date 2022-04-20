# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 01:27:44 2021

@author: Brandon
"""

# This program compares a name entered against a pre-defined string.
# If the entered name is not valid, it checks if there is one similar in the string using the "edit_distance" function
# edit_distance, which calculates how many characters are different between two strings. 
# The edit distance of "DOG" and "DIG" is 1, because changing the middle character would make the strings equivalent.

import edit_distance

#A few legal, acceptable Danish names / pre-defined list
legal_names = ['Thor', 'Bjork', 'Bailey', 'Anders', 'Bent', 'Bjarne', 'Bjorn', 
    'Claus', 'Emil', 'Finn', 'Jakob', 'Karen', 'Julie', 'Johanne', 'Anna', 'Anne', 
    'Bente', 'Eva', 'Helene', 'Ida', 'Inge', 'Susanne', 'Sofie', 'Rikkie', 'Pia', 
    'Torben', 'Soren', 'Rune', 'Rasmus', 'Per', 'Michael', 'Mads', 'Hanne', 
    'Dorte'
]

# Get name to test
user_name = input('Enter desired name:\n')

# Check to see if name is in the list
if user_name in legal_names:
    print('{} is an acceptable Danish name. Congratulations.'.format(user_name))

# If not in the list check for similar names with 1 character difference (<2)
else:
    print('{} is not acceptable.'.format(user_name))
    for name in legal_names:
        if edit_distance.distance(name, user_name)  < 2:
            print('You might consider: {},'.format(name), end=' ')
            break
    else:
        print('No close matches were found.')
print('Goodbye.')
