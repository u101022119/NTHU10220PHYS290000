# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 22:12:40 2014

"""

t=float(raw_input('please input the time interval of the satellite:'))
import math
h=(((6.67*10**-11)*(5.97*10**24)*(t**2)/4/(math.pi**2))**(0.3333333333333))-6417000
print 'The attitude of the satellite is',h,'meters'