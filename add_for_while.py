#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:37:29 2019

@author: kartiktanksali
"""

def for_sum(lst):
    sums = 0
    for i in lst:
        sums += i
    
    return sums

def while_sum(lst):
    sums = 0
    i=0
    
    while(i<len(lst)):
        sums += lst[i]
        i+=1
    return sums


lst = [1,2,3,4,10]

res = for_sum(lst)
print("Sum using for loop ",res)


res1 = while_sum(lst)
print("Sum using for loop ",res1)