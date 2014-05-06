# -*- coding: utf-8 -*-
"""
Created on Tue May 06 15:23:07 2014

@author: user
"""
def do_ntimes(f,n,s):
    index=0
    while index<n:
        f(s)
        index=index+1 
def print_word(s):
    print s
do_ntimes(print_word,4,'jj') 
    
