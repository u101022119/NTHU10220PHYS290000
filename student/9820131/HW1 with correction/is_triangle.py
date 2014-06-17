# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 16:54:21 2014

@author: user
"""

def is_triangle(x,y,z):
    if x+y>z and x+z>y and y+z>x:
        print 'Yes'
    else:
        print 'No'
x=int(input('x='))

y=int(input('y='))

z=int(input('z='))

is_triangle(x,y,z)