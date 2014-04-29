# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 16:32:09 2014

@author: user
"""
def catalan(n):
    n=int(raw_input('Enter a number:'))
    x=1    
    for i in range(n):
        y=(i*4.0+2)/(i+2)
        x = x*y
    print 'C',n,'=',x,
    
catalan(n)
