#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:04:27 2019

@author: kartiktanksali
"""

list1 = ["a","b","c"]
list2 = [1,2,3]

def combine(list1, list2):
    lst = []
    len1 = len(list1)
    len2 = len(list2)

    for index in range( max(len1, len2) ):
        if index+1 <= len1:
            lst += [list1[index]]

        if index+1 <= len2:
            lst += [list2[index]]

    return lst

res = combine(list1,list2)
print(res)