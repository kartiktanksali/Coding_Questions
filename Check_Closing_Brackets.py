#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:24:40 2019

@author: kartiktanksali
"""

from collections import Counter

string = input()
dic = Counter(string)

dic_hard = {"(":")","[":"]","{":"}"}

for k in dic.keys():
    if k in dic_hard:
        if dic[k]==dic[dic_hard[k]]:
            print("No issues with :",k,dic_hard[k])
        else:
            print("Issues with :",k,dic_hard[k])