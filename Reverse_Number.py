#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:08:19 2019

@author: kartiktanksali
"""

def reverse(x):
    reverse = 0
    n=x
    if x<0:
        x = x*-1

    while (x > 0):
        lastDigit = x % 10
        reverse = (reverse * 10) + lastDigit
        x = x//10

    if n<0:
        reverse =  reverse*-1
    
    if -2147483648 < reverse < 2147483647:
        return reverse
    else:
        return 0
    

x = int(input())
res = reverse(x)
print(res)