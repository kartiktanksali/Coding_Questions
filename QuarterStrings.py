#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:12:15 2019

@author: kartiktanksali
"""



def quarter(string):
    if 1<=q<=3:
        return string[0:4]+"Q1"
    elif 4<=q<=6:
        return string[0:4]+"Q2"
    elif 7<=q<=9:
        return string[0:4]+"Q3"
    elif 10<=q<=12:
        return string[0:4]+"Q4"
    
string = "2015-05-19"

q = string[5]+string[6]
q = int(q)

res = quarter(string)

print(res)