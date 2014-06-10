# -*- coding: utf-8 -*-
"""
Created on Wed Jun 04 18:18:53 2014

@author: Administrator
"""

class Date (object):
    """Represents the date of day."""
def print_date(date):
    print '%.2d/%.2d/%.2d' % (date.month, date.day, date.year)

A=Date()
A.month=2
A.day=25
A.year=1904
#print_date(A)

def increment_date(date,n):
    date.day=date.day+n
    L=[1,3,5,7,8,10]
    S=[4,6,9,11]
    while date.day>30 or date.month==2:        
        if date.month in S:
            date.day=date.day-30
            date.month=date.month+1
        elif date.month in L:
            if date.day==31:
                break
            else:
                date.day=date.day-31
                date.month=date.month+1
        elif date.month==2:
            if date.day<29:
                break
            elif (date.year%400==0) or (date.year%4==0 and date.year%100!=0):
               if date.day==29:
                   break
               else:
                   date.day=date.day-29
                   date.month=date.month+1
            else:
                date.day=date.day-28
                date.month=date.month+1
        else:
            date.day=date.day-31            
            date.month=1
            date.year=date.year+1
    return date

print_date(increment_date(A,3))        