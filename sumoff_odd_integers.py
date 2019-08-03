#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:17:04 2019

@author: kartiktanksali
"""

#Sum of odd integers

def sumOdd(n):
    for i in n:
        print(int((i+1)/2)**2)
        
        

lst = [1,3,5,7,4]
sumOdd(lst)