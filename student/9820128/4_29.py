# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:46:42 2014

@author: user
"""
from __future__ import division
class Point(object):
    """point"""
class Rectangle(object):
    """rectangle"""
class Time(object):
    """time"""    
    
blank=Point()
blank.x=3.0
blank.y=4.0
def distance_between_points(p):
    s=math.sqrt(p.x**2+p.y**2)
    print s
box=Rectangle()
box.width=100.0
box.height=200.0
box.corner=Point()
box.corner.x=1.0
box.corner.y=1.0

def print_point(p):
    print "(%g,%g)" % (p.x,p.y)
def move_rectangle(p,dx,dy):
    r=Point()
    r.x=p.corner.x+dx
    r.y=p.corner.y+dy
    return r
time=Time()
time.second=12
time.minute=50
time.hour=11
time2=Time()
time2.second=11
time2.minute=50
time2.hour=11
def print_time(p):
    print '%.2d:%.2d:%.2d' % (p.hour,p.minute,p.second)
def is_after(p1,p2):
    if p1.hour>p2.hour:
        return True
    else:
        if p1.minute>p2.minute:
            return True
        else:
            if p1.second>p2.second:
                return True
            else:
                return False

def into_seconds(p):
    s=p.hour*3600+p.minute*60+p.second
    return s

def is_after2(p1,p2):
    s1=seconds(p1)
    s2=seconds(p2)
    print s1>s2
def increment(p,seconds):
    s=into_seconds(p)
    print s
    s+=seconds
    print s
    p.hour=s//3600
    print p.hour
    p.minute=s % 3600 //60 
    print p.minute
    p.second=s-p.hour*3600-p.minute*60
    print s/60-int(s/60)
    print (s/60-int(s/60))*60
    print p.second
    return print_time(p)
