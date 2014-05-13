# -*- coding: utf-8 -*-
"""
Created on Mon May 12 12:57:36 2014

@author: Administrator
"""
def c(n):
    if n==0:
        return 1
    else:
        return (4*n-2)*c(n-1)/(n+1)
        
a=arange(100,dtype=float)
for x in a:
    if c(x)<=1.0e+9:
        print c(x)