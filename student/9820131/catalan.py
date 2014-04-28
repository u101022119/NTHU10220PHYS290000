# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\user\.spyder2\.temp.py
"""
def catalan():
    i=1
    t=1
    for i in range(1,1000):
        t=((4*(i-1)+2)/(i+1))*t
        i=i+1
        print t

catalan()