# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 20:52:05 2014


"""

x=float(raw_input('Please input the coordinate x:'))
y=float(raw_input('Please input the coordinate y:'))
r=(x**2.0+y**2.0)**0.5
import math 
theta=math.atan(y/x)/(2*math.pi)*360.0
print 'the polar is (',r,',',theta,'degrees)' 