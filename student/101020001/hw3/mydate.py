# -*- coding: utf-8 -*-
"""
Created on Tue May 13 18:46:07 2014

@author: wilson
"""

class Date():
    """it have month,day,and year"""

def print_date (date):
    print '%.4d/%.2d/%.2d' % (date.y,date.m,date.d)

date=Date()
date.y=2014
date.m=5
date.d=14

n=5000






def Leap_year (date):
    if date.y%400==0:
        return True
    elif date.y%100==0:
        return False
    elif date.y%4==0:
        return True
    else:
        return False
def increment_date(date,n):
    for i in range(n):
        if Leap_year (date):
            if date.m==2:
                if date.d==29:
                    date.d=1
                    date.m+=1
                else :
                    date.d+=1
            elif date.m in (4,6,9,11):
                if date.d==30:
                    date.d=1
                    date.m+=1
                else:
                    date.d+=1
                    
            elif date.m==13:
                date.m=1
                date.y+=1
                date.d=1
            elif date.m in (1,3,5,7,8,10,12):
                if date.d==31:
                    date.d=1
                    date.m+=1
                else:
                    date.d+=1
            
        else:
            if date.m == 2:
                if date.d==28:
                    date.d=1
                    date.m+=1
                else:
                    date.d+=1
            elif date.m in (4,6,9,11):
                if date.d==30:
                    date.d=1
                    date.m+=1
                else:
                    date.d+=1
            elif date.m==13:
                date.m=1
                date.y+=1
                date.d+=1
                    
            elif date.m in (1,3,5,7,8,10,12):
                if date.d==31:
                    date.d=1
                    date.m+=1
                else:
                    date.d+=1
    print print_date (date)



increment_date(date,n)
                