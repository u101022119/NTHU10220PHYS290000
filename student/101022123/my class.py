# -*- coding: utf-8 -*-
"""
Created on Tue May 13 17:21:15 2014

@author: user
"""
import math
class Point(object):
    pass
class Rectangle(object):
    pass

def distance_between_points(x1,x2,y1,y2):
    l=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return l

def move_rectangle(a,dx,dy):
    a.x += dx
    a.y += dy
    
c = Point()
c.x1=0
c.y1=0
c.x2=6
c.y2=8

print distance_between_points(c.x1,c.x2,c.y1,c.y2)

box = Rectangle()
box.corner = Point()
box.x = 10
box.y = 20


move_rectangle(box,10,20)
print box.x,box.y