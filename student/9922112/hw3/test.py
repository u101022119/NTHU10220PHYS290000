# -*- coding: utf-8 -*-
"""
Created on Wed Jun 04 18:25:55 2014

@author: Administrator
"""

class Date (object):
    """Represents the date of day."""
date=Date()
date.year=1600
 
print (date.year%400==0) or (date.year%4==0 and date.year%100!=0)

