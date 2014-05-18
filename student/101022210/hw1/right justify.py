# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 20:32:58 2014


"""

def right_justify():
    s=str(raw_input('please input a word to right justify:'))
    a=len(s)
    b=70-a
    print " "*b,s
    
right_justify()
