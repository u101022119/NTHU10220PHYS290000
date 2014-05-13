# -*- coding: utf-8 -*-
"""
Created on Mon May 12 07:54:15 2014

@author: Administrator
"""

n=input("Please enter n")
def factorial(n):
    if type(n)==int:
        if n>0:
            return n*factorial(n-1)
        elif n==0:
            return 1
        else:
            print'n must be an integer>=0'
    else:
        print'n must be an integer>=0'
print n,"! is",factorial(n)

        