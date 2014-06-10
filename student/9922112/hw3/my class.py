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

class rectangle(object):
 """Represents a rectangle attributes: width, height, corner."""
print 'we have a rectangle R with width 4.0, height,3.0,corner(1,1)'
R=rectangle()
R.width=4.0
R.height=3.0
R.corner=Point()
R.corner.x=1
R.corner.y=1

def move_rectangle(dx,dy):
    R.corner.x=R.corner.x+dx
    R.corner.y=R.corner.y+dy
    return [R.corner.x,R.corner.y]
D = raw_input("enter displacement as dx,dy")
D = map(float,D.split(','))
[dx,dy]=D

print 'the new corner of the rectangle is',move_rectangle(dx,dy)


