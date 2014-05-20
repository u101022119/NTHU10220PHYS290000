# -*- coding: utf-8 -*-
"""
Created on Tue May 13 16:58:05 2014

@author: user
"""

class Time(object):
    """pass"""
    
def print_time(t):
    print"%.2d:%.2d:%.2d" % (t.hour,t.minute,t.second)
    
a=Time()
a.hour=1
a.minute=2
a.second=3

b=Time()
b.hour=2
b.minute=2
b.second=3

print_time(a)

def bigsmall(t1,t2):
    a=t1.hour *3600 + t1.minute*60 + t1.second
    b=t2.hour *3600 + t2.minute*60 + t2.second
    if a<b:
        print "true"
    
    else:
        print "false"
    
def is_after(x,y):
    bigsmall(x,y)
    
    
def increment_pure(t1,increase):
    sum = Time()
    sum.second = t1.second + increase
    sum.minute=t1.minute
    sum.hour=t1.hour
    
    if sum.second >= 60:
        sum.second-=60
        sum.minute+=1
    
    if sum.minute >= 60:
        sum.minute-=60
        sum.hour+=1
        
    return sum
    
def mul_time(t1,mul):
    new = Time()
    new.second = t1.second   * mul
    new.minute = t1.minute   * mul
    new.hour   = t1.hour     * mul
    
    if new.second >= 60:
        new.second-=60
        new.minute+=1
    
    if new.minute >= 60:
        new.minute-=60
        new.hour+=1
        
    return new
    
def average_pace(t,n):
    mul_time(t,1.0/n)