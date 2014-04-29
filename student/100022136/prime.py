# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 17:26:08 2014

@author: user
"""
import math
prime=[2]
for i in range(3,10001):
    v=math.sqrt(i)
    for j in prime:
        if(j>v):
            prime.append(i)
            break
        elif(i%j==0):
            break
print(prime)
