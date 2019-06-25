#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:25:34 2019

@author: kartiktanksali
"""

#Kadane's Algorithm

lst = [-2,3,2,-1]

max_sum_global = max_sum_current = lst[0]

for i in range(1,len(lst)):
    max_sum_current = max(lst[i],lst[i]+max_sum_current)
    if max_sum_current > max_sum_global:
        max_sum_global = max_sum_current
        
print(max_sum_global)

