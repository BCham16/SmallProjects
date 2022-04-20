# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 05:00:54 2021

@author: Brandon
"""

import time

print('For the formula:\nAx + By = C\nPlease enter A, B, & C')
a = int(input('Input A1: '))
b = int(input('Input B1: '))
c = int(input('Input C1: '))

d = int(input('Input A2: '))
e = int(input('Input B2: '))
f = int(input('Input C2: '))

y = int()
z = int()
complete = int()

#(ax + by = c) & (dx + ey = f)
test = test2 = bool('false')
for z in range(-10,11):
    if complete == 1:
        z -=1
        break
    for y in range (-10,11):
        print('\ntrying A={} and B={}'.format(z, y))
        test = bool(a*z + b*y == c)
        test2 = bool(d*z + e*y == f)
        time.sleep(0.1)
        if test and test2 == bool('true'):
            print('Answer Found ^ !!')
            complete = 1
            break
        else:
            print('Tests Failed: {} + {} = {} not {}'.format(a*z, b*y, (a*z + b*y), c))

print('The Answer is: A={} and B={}\n'.format(z,y)) if complete == 1 else print('No solution')
print('{}*{} + {}*{} = {} and {}*{} + {}*{} = {}'.format(a, z, b, y, c, d, z, e, y, f))
print('{} + {} = {} and {} + {} = {}'.format(a*z, b*y, c, d*z, e*y, f))
