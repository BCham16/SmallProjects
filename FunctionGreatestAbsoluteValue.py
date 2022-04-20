# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 19:48:11 2021

@author: Brandon
"""

final_answer = 0

def max_magnitude(user_val1, user_val2):
    if user_val1 < 0 and user_val2 < 0:
        final_answer = user_val1 if user_val1 < user_val2 else user_val2
    elif user_val1 < 0:
        final_answer = user_val1 if (user_val1 * -1) > user_val2 else user_val2
    elif user_val2 < 0:
        final_answer = user_val1 if user_val1 > (user_val2 * -1) else user_val2
    else:
        final_answer = user_val1 if user_val1 > user_val2 else user_val2
    return final_answer


if __name__ == '__main__':
    user_val1 = int(input())
    user_val2 = int(input())
    
    
    print(max_magnitude(user_val1, user_val2))
    