# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 15:56:30 2014

@author: user
"""

import math
def satellite():
    T=float(raw_input('Put the period of the satellite:'))
    G=6.67*10**(-11)   
    M=5.97*10**24
    a=((G*M*T*T)/(4*math.pi**2))**0.3333333333333333
    h=a*10**(-3)-6417
    return h

print satellite()