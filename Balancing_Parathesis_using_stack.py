#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:27:45 2019

@author: kartiktanksali
"""

#Balacing the paranthesis using Stack

paranthesis_dict = {"(":")","[":"]","{":"}"}

def BalanceIt(string):
    stack = []
    top=-1
    for i in string:
        if i in paranthesis_dict.keys():
            stack.append(i)
            top+=1
            print(stack)
        elif i in paranthesis_dict.values():
            if (len(stack)>0) and (i == paranthesis_dict[stack[top]]):
                stack.pop()
                top-=1
                print(stack)
            else:
                return False
    
    if len(stack)==0:
        return True

    
    

string = input("Enter a expression: ")
res = BalanceIt(string)
print("Balanced" if res==True else "Unbalanced")