#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:13:05 2019

@author: kartiktanksali
"""

str1 = "abc"
str2 = "racecar"

def check_palindrome(string):
    st1 = string
    st2 = string[::-1]
    if st1 == st2:
        l = int(len(st1))
        h = int(len(st1)/2)
        if h%2==0:
            print(f"({st1[0:h]})({st1[h:l]})")
        else:
            print(f"({st1[0:h]}){st1[h]}({st1[h+1:l]})")
            
        print("Palindrome")
    else:
        print("Not a palindrome")
        
check_palindrome(str1)
check_palindrome(str2)
