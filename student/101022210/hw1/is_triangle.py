# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 21:24:42 2014


"""

def is_triangle():
    a=int(raw_input('Please input first side of the triangle:'))
    b=int(raw_input('Please input second side of the triangle:'))
    c=int(raw_input('Please input third side of the triangle:'))
    d=a-b
    if d<0:
        d=-d
    if a+b>c:
        if d<c:
            print 'This can be the triangle!'
        else:
                print 'This cannot be the triangle!'        
                return
    else:
            print 'This cannot be the triangle!'
            return
        
is_triangle()