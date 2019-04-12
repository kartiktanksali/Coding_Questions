#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:18:20 2019

@author: kartiktanksali
"""

#lst = [1,2,3]
#
#sub_lst = []
##
#def subarraySum(nums, k):
#        res = 0
#        count=0
#        for i in range(len(nums)):
#            count=0
#            for j in range(i, len(nums)):
#                count+=1
#                if sum(nums[i:j+1]) == k:
#                    res += 1
#                    sub_lst.append(count)
#        return max(sub_lst)
#    
#res = subarraySum(lst,5)
#print(res)
#sub_lst = []
#def printSubArrays(arr, start, end): 
#      
#    # Stop if we have reached the end of the array     
#    if end == len(arr): 
#        return
#      
#    # Increment the end point and start from 0 
#    elif start > end: 
#        return printSubArrays(arr, 0, end + 1) 
#          
#    # Print the subarray and increment the starting 
#    # point 
#    else: 
#        sub_lst.append(arr[start:end + 1])
#        return printSubArrays(arr, start + 1, end) 
#          
## Driver code 
#arr = [1, 2, 3, 4] 
#printSubArrays(arr, 0, 0)
#
#for i in sub_lst:
#    if sum(i)==5:
#        print(i)

#def sums(x):
#    x+=x
#
#
#lst = [1,2,3,4,5]
#
#sub_lst = []
#temp_lst = []
#for i in range(len(lst)):
#    temp_lst=[]
#    for j in range(i,len(lst)):
#        temp_lst.append(lst[j])
#    s = map(sums,temp_lst)
#    if s==5:
#        sub_lst.append(temp_lst)
#        
#
#print(sub_lst)



#nums = [1,2,3,4,5,6]
#k=6
#h = {0: 1}
#s = 0
#c = 0
#count=0
#for i in nums:
#    s += i
#    if s - k in h:
#        c += h[s - k]
#        count+=1
#    if s in h:
#        h[s] += 1
#    else:
#        h[s] = 1
#print(c)
#print(count)



def atMostSum(arr,k): 
    _sum = 0
    cnt = 0
    maxcnt = 0
      
    for i in range(len(arr)): 
  
        if ((_sum + arr[i]) <= k): 
            _sum += arr[i] 
            cnt += 1
          
        elif(sum != 0): 
            _sum = _sum - arr[i - cnt] + arr[i] 
          
        maxcnt = max(cnt, maxcnt) 
  
    return maxcnt 

arr = [1,2,3,4,5]
k = 6

res = atMostSum(arr,k)
print(res)





