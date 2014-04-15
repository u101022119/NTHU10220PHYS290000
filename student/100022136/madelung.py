# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 16:50:48 2014

@author: user
"""
import math
L=200
M=0
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if(i==0 and j==0 and k==0):
                M+=0
            elif((i+j+k)%2==0):
                M+=1/math.sqrt(i*i+j*j+k*k)
            else:
                M-=1/math.sqrt(i*i+j*j+k*k)
print M