#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
    

s = "I use hackerrank to improve my programming"
t = "programming hackerrank"

res = MissingWords(s,t)
print(res)