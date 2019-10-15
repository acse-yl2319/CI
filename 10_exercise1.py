# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:34:50 2019

@author: 34783
"""

# question1
def fizz_buzz(x):
    if (x%3==0) & (x%5==0):
        return "fizz buzz"
    elif x%3==0:
        return "fizz"
    elif x%5==0:
        return "buzz"

print(fizz_buzz(5))

