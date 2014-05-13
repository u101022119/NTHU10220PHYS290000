# -*- coding: utf-8 -*-
"""
Created on Fri May 09 11:11:57 2014

@author: Administrator
"""
import math
C = [input("enter x coordinate"),input("enter y coordinate")]
[x,y]=C
r=math.sqrt(x**2+y**2)
a=math.degrees(math.atan2(y,x))
P=[r,a]
print "the polar coordinate is",P









    