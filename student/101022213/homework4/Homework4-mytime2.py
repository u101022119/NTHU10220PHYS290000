# -*- coding: utf-8 -*-
"""
Created on Mon Jun 02 21:17:17 2014

@author: USER
"""

class Time(object):
    """Represents the time of day.attributes: hour, minute, second"""
    
def cmp(t1,t2):
    if t1.hour/24.0>1.0 or t1.minute/60.0>1 or t1.second/60.0 > 1 or t2.hour/24.0 >1 or t2.minute/60.0>1 or t2.second/60.0 >1:
        print 'the time in t1 or t2 is wrong'
    else:
        if t1.hour > t2.hour:
            print 't1 is after t2'
        elif t1.hour < t2.hour:
            print 't2 is after t1'
        else:
            if t1.minute > t2.minute:
                print 't1 is after t2'    
            elif t1.minute < t2.minute:
                print 't2 is after t1'
            else:
                if t1.second > t2.second:
                    print 't1 is after t2'
                elif t1.second < t2.second:
                    print 't2 is after t1'
                else:
                    print 't1 = t2'
	
t1 = Time()
t2 = Time()

t1.hour = 2
t1.minute = 20
t1.second = 23

t2.hour = 2
t2.minute = 20
t2.second = 23
	
cmp(t1,t2)

t1.hour = input("the first time hour : ")
t1.minute = input("the first time minute : ")
t1.second = input("the first time second : ")
t2.hour = input("the second time hour : ")
t2.minute = input("the second time minute : ")
t2.second = input("the second time second : ")

cmp(t1,t2)
