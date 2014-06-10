# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 21:31:25 2014


"""

h=float(raw_input('Please input the high of the tower:'))
t=float(raw_input('Please input the time interval of the ball falling:'))

h1=h-4.9*t*t

print 'The height of the ball above the ground at',t,'is',h1,'meters'