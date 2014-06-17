# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 15:56:11 2014

@author: user
"""

def right_justify(s):
    i=0
    while i<(70-len(s)):
        print ' ',
        i=i+1
    print s

right_justify('apple')