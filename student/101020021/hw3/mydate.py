# -*- coding: utf-8 -*-
"""
Created on Tue May 13 17:07:01 2014

@author: user
"""

class Date(object):
    ''''''

def ifleapyear(year):
    if year % 400 ==0 :
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 ==0:
        return True
    else:
        return False
        
def increment_date(date,n):
        for i in range(n):
            if date.month==12 and date.day==31:
                date.year+=1
                date.month=1
                date.day=1
            elif ifleapyear(date.year) and date.month==2 and date.day==29 :
                date.month+=1
                date.day=1              
            elif (not ifleapyear(date.year)) and date.month==2 and date.day==28:
                date.month+=1
                date.day=1
            elif date.month in ( 4, 6, 9, 11 ) and date.day==30:
                date.month+=1
                date.day=1
            elif date.day==31:
                date.month+=1
                date.day=1
            else:
                date.day+=1
        
date=Date()
date.year=2005
date.month=12
date.day=31

increment_date(date,5000)
print '(%d : %d : %d)' % (date.year,date.month,date.day)