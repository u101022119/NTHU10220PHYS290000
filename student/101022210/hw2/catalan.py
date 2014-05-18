# -*- coding: utf-8 -*-
"""
Created on Sun May 18 23:12:58 2014
"""

def catalan(n):
    if n==0:
        return 1
    else:
        return int((4*n-2.0)/(n+1.0)*catalan(n-1))
c=int(raw_input('Please input an integer:'))
for i in range(c+1):
    print catalan(i), 
    