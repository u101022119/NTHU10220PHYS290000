# -*- coding: utf-8 -*-
"""
Created on Fri May 09 23:10:09 2014

@author: Administrator
"""

T=input("the length of three sticks [a,b,c]:")
T.sort()
T=[int(T[0]),int(T[1]),int(T[2])]
print T
[a,b,c]=T
if c<a+b:
    print "yes!"
else:
    print "No!"