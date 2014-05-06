# -*- coding: utf-8 -*-
"""
Created on Tue May 06 13:01:37 2014

@author: user
"""
def right_justify(s):
    start=70-len(s)
    index=0   
    while index<=start:
        print ''
        index=index+1
    while index>start:
        if index<70:
            print s[index-start-1]
        index=index+1        
right_justify('banana')