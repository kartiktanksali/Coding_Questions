#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:10:23 2019

@author: kartiktanksali
"""

#String Permutation

def create_hashmap(string):
    hash_map = {}
    
    for i in string:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    
    return hash_map

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")


str1_map = create_hashmap(str1)
str2_map = create_hashmap(str2)

if str1_map == str2_map:
    print("One is permutation of another")
else:
    print("They are not")