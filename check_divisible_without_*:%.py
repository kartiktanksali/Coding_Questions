#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:43:02 2019

@author: kartiktanksali
"""

import math


def isDivisible(number1,number2):
    n1 = number1
    n2 = number2
    for i in range(number2):
        if number1 == 0:
            print(n1," Divided by ",n2," is ",i)
            break
        elif number1 < 0:
            print(n1," Divided by ",n2," is ",math.floor(n1/n2)," with a remainded of ",n1%n2)
            break
        
        number1 -= number2

    
number1 = 6
number2 = 4

res = isDivisible(number1,number2)
