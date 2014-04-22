# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 16:59:48 2014

@author: user
"""
class Point(object):
    """Represents a point in 2-D space."""

class Rectangle(object):
    """Represents a rectangle.
    
    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def move_rectangle(box,dx,dy):
    box.corner.x+=dx
    box.corner.y+=dy
    #Notice:box is mutable,so after done this step,the box will really move.
    
move_rectangle(box,12.0,13.0)
print box.corner.x
print box.corner.y