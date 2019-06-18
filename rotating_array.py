#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:23:09 2019

@author: kartiktanksali
"""

#Array Rotation

lst = [1,2,3,4,5,6,7]

nr = int(input("Enter the number of rotations: "))

for i in range(nr):
    temp = lst[0]
    for j in range(len(lst)-1):
        lst[j] = lst[j+1]
    lst[len(lst)-1] = temp
    
print(lst)