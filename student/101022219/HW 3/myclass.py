# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 16:30:28 2014

@author: User
"""
import copy, math

class Point(object):
    ''''''
    
class Rectangle(object):
    ''''''

def distance_between_points(a,b):
    print ((a.x-b.x)**2 + (a.y-b.y)**2)**(1.0/2.0)
    
def move_rectangle(rec,dx,dy):
   rec.corner.x += dx
   rec.corner.y += dy
   
def move_rectangle_ver2(rec,dx,dy):
    new_rec=copy.deepcopy(rec)
    new_rec.corner.x += dx
    new_rec.corner.y += dy
    return new_rec
    

p1=Point()
p2=Point()
p1.x=5
p1.y=6
p2.x=13
p2.y=18

box1=Rectangle()
box1.corner=Point()
box1.width=12
box1.height=13
box1.corner.x=16
box1.corner.y=17


distance_between_points(p1,p2)

box2=move_rectangle_ver2(box1,7,8)
print box1.corner.x,box1.corner.y
print box2.corner.x,box2.corner.y

move_rectangle(box1,7,8)
print box1.corner.x,box1.corner.y