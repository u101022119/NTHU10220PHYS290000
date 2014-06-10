# -*- coding: utf-8 -*-
"""
Created on Wed May 14 11:54:26 2014

@author: user
"""

from matplotlib.pylab import *

def mandelbrot(c):
    z=0    
    for i in xrange(100):
        z=z*z+c
        if sqrt(z.real**2+z.imag**2)>2:
            return False
    return True

xlist=[x*0.01 for x in range(-200, 201)]
ylist=[y*0.01 for y in range(-200, 201)]
show=empty([len(xlist), len(ylist)], int)
for i in xrange(len(xlist)):
    for j in xrange(len(ylist)):
        c=complex(xlist[i], ylist[j])
        if mandelbrot(c)==True:
            show[i, j]=0
        elif mandelbrot(c)==False:
            show[i, j]=1
imshow(show, origin="lower")
gray()
show()