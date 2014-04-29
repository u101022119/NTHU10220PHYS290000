# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:59:45 2014

@author: user
"""
import math

class Point(object):
    """Represents a point in 2-D space."""
    
print Point

blank = Point()

blank.x = 3.0
blank.y = 4.0

print '(%g, %g)' % (blank.x, blank.y)

distance = math.sqrt(blank.x**2 + blank.y**2)
print distance

def distance_between_points(x,y,a,b):
    d = math.sqrt((x-a)**2 + (y-b)**2)
    print d
    
distance_between_points(8,6,0,0)

class Rectangle(object):
    """Represents a rectangle.
    
    attributes: "width, height, corner"
    """
    
Dewi = Rectangle()
Dewi.width = 100.0
Dewi.height = 200.0
Dewi.corner = Point()
Dewi.corner.x = 0.0
Dewi.corner.y = 1.0    

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p
    
def print_point(p):
    print '(%g, %g)' % (p.x, p.y)
    
center = find_center(Dewi)
print_point(center)

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print Dewi.width
print Dewi.height

grow_rectangle(Dewi, 100, 50)

print Dewi.width
print Dewi.height

def move_rectangle(rect):