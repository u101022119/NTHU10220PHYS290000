# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 04:11:27 2014

@author: liaoyukai
"""
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import numpy as np



def Mandelbrot(c):
    z=complex(0,0)    
    for i in range(100):
        s=z**2
        if abs(z) >=2:
            return 2
        z=s+c
    return s.real
    

        
N=1000

       
#x=linspace(-2,2,N+1)
#y=linspace(-2,2,N+1)
#c=complex(x,y)

s=empty([N,N],float)

for i in range(N):
    x=-2+4.0*i/N
    for j in range(N):
        y=-2+4.0*j/N
        c=complex(x,y)
        s[j,i]=Mandelbrot(c)

imshow(s,origin="lower",extent=[-2,2,-2,2])
jet()
show()