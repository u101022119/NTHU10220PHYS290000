# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 19:28:17 2014

@author: Sonic
"""

def catalan(n):
    if n==0:
        return 1
    else:
        return (4*n-2)/(n+1)*catalan(n-1)
n=float(raw_input("Put n right here!"))
if n<=1000000000:
   print catalan(n) 
else:
    print "Your n is too big!"