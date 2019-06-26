#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:40:11 2019

@author: kartiktanksali
"""
import math

def arrangeCoins(n):
    lst = []
    for i in n:
        k = -0.5 + math.sqrt(0.25 + 2 * i)
        lst.append(int(math.floor(k)))
    
    for i in lst:
        print(i)


n = [2,5,8]
print(arrangeCoins(n))