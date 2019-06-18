#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:54:07 2019

@author: kartiktanksali
"""

#URLify

def URLify(string):
    return string.replace(" ","%20")


string = input("Enter a string: ")
res = URLify(string)
print(res)