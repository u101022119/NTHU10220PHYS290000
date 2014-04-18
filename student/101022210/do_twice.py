# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 21:07:27 2014


"""

def do_twice(f,s):
    f(s)
    f(s)
    
def print_twice(s):
    print s
    print s
    
s=raw_input('Please input a words:')
do_twice(print_twice,s)

def do_four(f1,f2,s):
    f1(f2,s)
    f1(f2,s)
    
do_four(do_twice,print_twice,s)