# -*- coding: utf-8 -*-
"""
Created on Tue May 13 08:22:09 2014

@author: user
"""

s=1
n=0
while s<=1000000000:
	 print s
	 s=(4*n+2)*s/(n+2)
	 n=n+1