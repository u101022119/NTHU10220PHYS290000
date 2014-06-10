# -*- coding: utf-8 -*-
"""
Created on Tue Jun 03 16:56:40 2014

@author: user
"""
class Time (object):
    """Represents the time of day."""
def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hr, time.min, time.sec)

B=Time()
B.hr=3
B.min=30
B.sec=40


def is_after(t1,t2):
    t1=Time()
    t2=Time()
    while t1.
