#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:03:31 2019

@author: kartiktanksali
"""

#Find the squares

import math 
def CountSquares(arr):
    new_lst = []
    for i in arr:
        temp = i.split(" ")
        start = int(temp[0])
        end = int(temp[1])
        
        new_lst.append((math.floor(math.sqrt(end)) - math.ceil(math.sqrt(start)) + 1)) 
  
    return new_lst


lst = ["3 9","17 24"]

res = CountSquares(lst)
print(res)

