# -*- coding: utf-8 -*-
"""
Created on Tue May 20 17:27:09 2014

@author: user
"""

class Point(object):
 """Represents a point in 2-D space."""
a =Point()
b =Point()

def distance_between_points(a,b):
    distance = math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
    return distance
A = raw_input("enter point a as x,y")
A = map(float,A.split(','))
[a.x,a.y]=A

B = raw_input("enter point b as x,y")
B = map(float,B.split(','))
[b.x,b.y]=B

print distance_between_points(a,b)

