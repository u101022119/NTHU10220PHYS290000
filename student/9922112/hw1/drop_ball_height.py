# -*- coding: utf-8 -*-
"""
Created on Tue May 06 18:02:49 2014

@author: user
"""

h= float(raw_input('the height of the tower\n'))
t= float(raw_input('the time interval\n'))
def result(h,t):
    return h-0.5*9.8*t**2
print "the height of the ball above the ground is",result(h,t)

