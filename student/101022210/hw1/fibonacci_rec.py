# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 22:07:16 2014


"""
n=input('Please input the fibonacci number:' )
def fibonacci_rec(n):
    if n<0:
        pass
    elif not isinstance(n,int):
        pass
    else:
        if n==1:
            return 1
        elif n==2:
            return 1
        else:
            return fibonacci_rec(n-1) +fibonacci_rec(n-2)
def print_fibonacci(n):
    f1,f2=1,1
    if n<0:
        print 'fibonacci number cannot be negative'
    elif not isinstance(n,int):
        print 'fibonacci need to be integer'
    elif n==1:
        print '1'
    else:
        while f1<=fibonacci_rec(n):
            print f1,' '
            f1,f2=f2,f1+f2
fibonacci_rec(n)
print_fibonacci(n)