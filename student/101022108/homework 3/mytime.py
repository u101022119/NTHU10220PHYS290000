# -*- coding: utf-8 -*-
"""
Created on Mon May 19 08:27:30 2014

@author: Mark
"""

class Time:
    '''attributes hour, min, sec '''
def print_time(t):   
    print '%.2d:'%t.hour, '%.2d:'%t.min, '%.2d'%t.sec

def is_after(t1, t2):
    sum1 = t1.hour*60*60+t1.min*60+t1.sec
    sum2 = t2.hour*60*60+t2.min*60+t1.sec
    if sum1 > sum2: 
        return True
    else:
        return False
def increment_modifier(t1):
     sum1 = t1.hour*60*60+t1.min*60+t1.sec
     return sum1

def increment_pure(sec):
    t = Time
    t.hour = sec/3600
    t.min = (sec%3600)/60
    t.sec = (sec%60)/60.0
    return t

def mul_time(t, k):
    temp = increment_modifier(t)*k
    temp2 = increment_pure(temp)
    return temp2    
def average_pace(t, distance):
    return mul_time(t,1.0/distance)

t = Time
t.hour = 10
t.min = 10
t.sec = 10
print_time(t)
