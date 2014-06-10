# -*- coding: utf-8 -*-
"""
Created on Tue Jun 03 16:56:40 2014

@author: user
"""
class Time (object):
    """Represents the time of day."""
    def __init__(self, hr=0, min=0, sec=0):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hr, self.min, self.sec)
    def __add__(self, other):
        seconds =convertsec(self)+convertsec(other)
        return converttime(seconds)

def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hr, time.min, time.sec)

B=Time()
B.hr=0
B.min=4
B.sec=0

A=Time()
A.hr=8
A.min=00
A.sec=40

def converttime(sec):
    T=Time()
    T.hr=sec//3600
    T.min=(sec%3600)//60
    T.sec=((sec%3600)%60)
    return T
    
#print_time(converttime(260))

def convertsec(time):
    return time.hr*3600+time.min*60+time.sec

def is_after(t1,t2):
    convertsec(t1)>convertsec(t2)
    print 'A>B is',convertsec(t1)>convertsec(t2)   
#is_after(A,B)

def increment_modifier(self,sec):
    sec+=convertsec(self)
    self=converttime(sec)
    return self
#print_time(increment_modifier(B,30)) 

def increment_pure(time,sec):
    S=sec+convertsec(time)
    return converttime(S)
#print_time(increment_pure(B,40)) 
    
def mul_time(time,n):
    S=convertsec(time)*n
    return converttime(S)
#print_time(mul_time(B,60))

def average_pace(time,distance):
    return convertsec(time)/distance
#print 'the average pace is ',average_pace(B,4),'sec per mile'

def __init__(self, hour=0, minute=0, second=0):
    self.hour = hour
    self.minute = minute
    self.second = second

#L=Time(3,20)
#K=Time(9,40,17)
#print L+K

   
    
