# -*- coding: utf-8 -*-
"""
Created on Mon May 12 09:04:48 2014

@author: Administrator
"""


def fib(x):
    if x<0 :
        print'error'
    elif x < 2:
        return x
    else: 
        return fib(x-2)+fib(x-1)
def fib_series(n):
    if n <=0 or type(n)!=int:
        print'n must be an positive integer'
    else:
        print fib(n-1)
        if n-1>0:
            fib_series(n-1)
n = input("Enter positive integer n to show the first n Fibonacci numbers(from 0th term)")
fib_series(n)
        

     