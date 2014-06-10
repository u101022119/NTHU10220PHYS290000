# -*- coding: utf-8 -*-
"""
Created on Fri May 09 10:26:42 2014

@author: Administrator
"""
import math
from fractions import Fraction
T =float(raw_input("Please enter the period(seconds) of the satelite:"))
G=6.67e-11#m.k.s
M=5.97e24#kg
R=6417000#m
h=math.pow(G*M*T**2/(4*math.pi**2),Fraction(1,3))-R
print "the height of the satelite above ground is",h,"meters"