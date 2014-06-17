# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 15:54:54 2014

@author: user
"""

def factorial_rec(n):
    if n < 0:
        print 'None'
    elif n == 0:
        return 1
    else:
        rec = factorial_rec(n-1)
        result = n*rec
        return result
    
a = int(raw_input('Put an integer:'))
if a < 0:
    print 'None'
else:
    print factorial_rec(a)
