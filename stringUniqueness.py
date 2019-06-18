#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:36:20 2019

@author: kartiktanksali
"""

#Check if all the characters of a string are unique

def StrUnique(string):
    if len(string) > 256:
        return "Not Unique"
    else:
        lst = [False] * 128
        
        for i in range(len(string)):
            val = ord(string[i])
            if lst[val]:
                return "Not Unique"
            lst[val] = True
        return "Unique"


string = input("Enter a string: ")

res = StrUnique(string)
print(res)