# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\user\.spyder2\.temp.py
"""

class Point(object):
    """Represents a point in 2-D space."""
print Point

blank=Point()
blank.x=3.0
blank.y=4.0
print '("%g,%g")'%(blank.x,blank.y)





def distance_between_points(point1,point2):
##this function can only use on the object with the type of Point  
    r=math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)
    return r

point1=Point()
point1.x=3.0
point1.y=4.0

point2=Point()
point2.x=6.0
point2.y=7.0

print distance_between_points(point1,point2)