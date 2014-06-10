# -*- coding: utf-8 -*-
"""
Created on Tue May 27 16:47:43 2014

@author: user
"""

import copy

class Point(object):
    pass
    
class Rectangle(object):
    pass
    
def distance_between_point(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def move_rectangle(a,dx,dy):
    a.x += dx
    a.y += dy
    

p = Point()
p.x1 = 0
p.y1 = 0
p.x2 = 3
p.y2 = 4
print distance_between_point(p.x1,p.y1,p.x2,p.y2)

box = Rectangle()
box.corner = Point()

box2 = copy.deepcopy(box)

box.corner.x = 100
box.corner.y = 200
box2.corner.x = 100
box2.corner.y = 200

move_rectangle(box.corner,20,30)
print box.corner.x,box.corner.y

move_rectangle(box2.corner,40,60)
print box2.corner.x,box2.corner.y
