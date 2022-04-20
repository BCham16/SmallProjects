# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:42:09 2021

@author: Brandon
"""




def exact_change(user_total):
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    
    if int(user_total) >= 100:
        num_dollars = int(user_total / 100)
        user_total = int(user_total) % 100
    if int(user_total) >= 25:
        num_quarters = int(user_total / 25)
        user_total = int(user_total) % 25
    if int(user_total) >= 10:
        num_dimes = int(user_total / 10)
        user_total = int(user_total) % 10
    if int(user_total) >= 5:
        num_nickels = int(user_total / 5)
        user_total = int(user_total) % 5
    if int(user_total) > 0:
        num_pennies = user_total
        user_total = int(user_total) - int(num_pennies)
        
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    user_total = int(input())

    print ('{:.0f} {}'.format((exact_change(user_total)[0]), 'dollars' if exact_change(user_total)[0] > 1 else 'dollar')) if exact_change(user_total)[0] > 0 else 0
    print ('{:.0f} {}'.format((exact_change(user_total)[1]), 'quarters' if exact_change(user_total)[1] > 1 else 'quarter')) if exact_change(user_total)[1] > 0 else 0
    print ('{:.0f} {}'.format((exact_change(user_total)[2]), 'dimes' if exact_change(user_total)[2] > 1 else 'dime')) if exact_change(user_total)[2] > 0 else 0
    print ('{:.0f} {}'.format((exact_change(user_total)[3]), 'nickels' if exact_change(user_total)[3] > 1 else 'nickel')) if exact_change(user_total)[3] > 0 else 0
    print ('{:.0f} {}'.format((exact_change(user_total)[4]), 'pennies' if exact_change(user_total)[4] > 1 else 'penny')) if exact_change(user_total)[4] > 0 else 0
    if sum(exact_change(user_total)) <= 0:
        print('no change')
