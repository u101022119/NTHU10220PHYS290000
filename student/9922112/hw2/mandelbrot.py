# -*- coding: utf-8 -*-
"""
Created on Tue May 20 13:44:11 2014

@author: Administrator
"""

import cmath
def mandelbrot(c,n):           
    z=0
    while n>0:
        z=z**2+c
        n=n-1
    return abs(z)


x=range(-2,3,1)
y=range(-2,3,1)

for a in x:
    for b in y:
        k=complex(a,b)
        if  mandelbrot(c,n)>2
        
