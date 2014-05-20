# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 21:51:10 2014


"""
n=input('Please input the factorial number:')
def factorial_rec(n):
    if n<0:
        print 'factorial number cannot be negative'
    elif not isinstance(n,int):
        print 'factorial number need to be integer'
    elif n==0:
        return 1
    else:
        return n*factorial_rec(n-1)
a=factorial_rec(n)
if not isinstance(a,int):
    pass
else:
    print a