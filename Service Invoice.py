# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 02:19:57 2021

@author: Brandon
"""

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

first_service = input('\nSelect first service:\n')
second_service = input('Select second service:\n')

prices = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}
first_price = prices[first_service] if first_service != '-' else 0
second_price = prices[second_service] if second_service != '-' else 0
total = int(first_price) + int(second_price)

print("\nDavy's auto shop invoice\n")

if first_price != 0:
    print('Service 1: {}, ${}'.format(first_service, first_price))
else:
    print('Service 1: No service')
    
if second_price != 0:
    print('Service 2: {}, ${}'.format(second_service, second_price))
else:
    print('Service 2: No service')
print('\nTotal: ${}'.format(total))