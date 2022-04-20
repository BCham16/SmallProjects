# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:42:09 2021

@author: Brandon
"""

amount = input('Enter an amount: ')
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

print()
if int(amount) >= 100:
    dollars = int(amount) / 100
    amount = int(amount) % 100
if int(amount) >= 25:
    quarters = int(amount) / 25
    amount = int(amount) % 25
if int(amount) >= 10:
    dimes = int(amount) / 10
    amount = int(amount) % 10
if int(amount) >= 5:
    nickels = int(amount) / 5
    amount = int(amount) % 5
if int(amount) > 0:
    pennies = amount
    amount = int(amount) - int(pennies)
if int(amount) == 0:
    print ('{} {}'.format(int(dollars), 'Dollars' if int(dollars) > 1 else 'Dollar')) if int(dollars) > 0 else 0
    print ('{} {}'.format(int(quarters), 'Quarters' if int(quarters) > 1 else 'Quarter')) if int(quarters) > 0 else 0
    print ('{} {}'.format(int(dimes), 'Dimes' if int(dimes) > 1 else 'Dime')) if int(dimes) > 0 else 0
    print ('{} {}'.format(int(nickels), 'Nickels' if int(nickels) > 1 else 'Nickel')) if int (nickels) > 0 else 0
    print ('{} {}'.format(int(pennies), 'Pennies' if int(pennies) > 1 else 'Penny')) if int(pennies) > 0 else 0
if int(dollars) + int(quarters) + int(dimes) + int(nickels) + int(pennies) == 0:
    print ('No change')