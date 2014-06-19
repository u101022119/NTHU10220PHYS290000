# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 15:26:56 2014

@author: Administrator
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
    def __cmp__(self, other):
        t1 = self.hr, self.min, self.sec
        t2 = other.hr, other.min, other.sec
        return cmp(t1, t2)

def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hr, time.min, time.sec)
    
#L=Time(9,40,16)
#K=Time(9,40,17)
#print cmp(L,K)