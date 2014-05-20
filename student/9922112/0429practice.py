# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:56:07 2014

@author: user
"""
class Point(object):
     """Represents a point in 2-D space."""
print Point 
blank = Point()
blank.x = 3.0
blank.y = 4.0

pta = Point()
pta.x = 0.0
pta.y = 0.0
ptb = Point()
ptb.x = 3.0
ptb.y = 4.0

def distance_between_points (a,b):
    dx = a.x-b.x
    dy = a.y-b.y
    distance = math.sqrt(dx**2+dy**2)
    print distance
distance_between_points (pta,ptb)

