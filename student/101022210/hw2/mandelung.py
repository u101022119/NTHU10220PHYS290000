# -*- coding: utf-8 -*-
"""
Created on Sun May 18 23:38:40 2014


"""
import math
L=int(raw_input('Input the value L:'))
M=0
for i in range(-L,L+1,1):
    for j in range(-L,L+1,1):
        for k in range(-L,L+1,1):
            if i==0 and j==0 and k==0:
                M=M+0
            elif (i+j+k)%2==0:
                M=M+1/math.sqrt(i**2+j**2+k**2)
            else:
                M=M-1/math.sqrt(i**2+j**2+k**2)
print M