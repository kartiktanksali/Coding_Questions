#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:30:30 2019

@author: kartiktanksali
"""

#Missing words
def MissingWords(s,t):
    new_s = s.split(" ")
    new_t = t.split(" ")
    lst = []
    

    for i in range(len(new_s)):
        flag = 0
        for j in range(len(new_t)):
            if new_s[i] == new_t[j]:
                flag = 1
            
        if flag == 0:
            lst.append(new_s[i])
    
    return lst
    

s = "I like cheese"
t = "like"

res = MissingWords(s,t)
print(res)