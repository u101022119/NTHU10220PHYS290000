# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 17:01:28 2014

@author: user
"""

class Time(object):
    """Represents the time of day.attributes: hour, minute, second"""

#t = Time()
#t.hour = 11
#t.minute = 59
#t.second = 30

def print_time(x):
    print '%g : %g : %g ' % (x.hour, x.minute, x.second)
    

t1 = Time()
t2 = Time()  
newtime = Time()

t1.hour = input("the first time hour : ")
t1.minute = input("the first time minute : ")
t1.second = input("the first time second : ")
t2.hour = input("the second time hour : ")
t2.minute = input("the second time minute : ")
t2.second = input("the second time second : ")


def is_after(t1,t2):
    while t1.hour - t2.hour == 0 + t1.minute - t2.minute == 0 + t1.second - t2.second == 0:
        return "ture"
    else:
        print "False"
        
        

def increment(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1



newtime = Time()
newtime.hour = t1.hour
newtime.minute = t1.minute
newtime.second = t1.second


def increment_pure(seconds):
    
    newtime.second += seconds
    if newtime.second >= 60:
       newtime.second -= 60
       newtime.minute += 1

    if newtime.minute >= 60:
       newtime.minute -= 60
       newtime.hour += 1

        


