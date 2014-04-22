# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\user\.spyder2\.temp.py
"""

>>>class Point(object):
...     """Represents a point in 2-space."""
... 
>>> print Point
<class '__main__.Point'>
>>> WTF is Point
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'WTF' is not defined
>>> blank = Point()
>>> print blank
<__main__.Point object at 0x000000000210DE80>
>>> blank.x = 10.0
>>> blank.y = 12.0
>>> print blank
<__main__.Point object at 0x000000000210DE80>
>>> print '(%g, %g)' % (blank.x, blank.y)
(10, 12)
>>> distance = math.sqrt(blank.x**2 + blank.y**2)
>>> print distance
15.6204993518
>>> blank.x = 5.0
>>> blank.y = 12.0
>>> distance
15.620499351813308
>>> distance = math.sqrt(blank.x**2 + blank.y**2)
>>> distance
13.0
>>> print_point(blank)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print_point' is not defined
>>> print_Point(blnak)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print_Point' is not defined
>>> def print_point(p):
...     print '(%g, %g)' % (p.x, p.y)
... 
>>> print_point(blank)
(5, 12)
>>> def distance_between_points(p,q):
...     x1 = p.x
...     x2 = q.x
...     y1 = p.y
...     y2 = q.y
...     dx = x2 - x1
...     dy = y2 - y1
...     sq = dx**2 + dy**2
...     distance = math.sqrt(sq)
...     print distance
... 
>>> dark = Point()
>>> print dark
<__main__.Point object at 0x0000000009875198>
>>> dark.x = 7.0
>>> dark.y = 17.0
>>> distance_between_points(blank, dark)
5.38516480713
>>> print_point(blank)
(5, 12)
>>> print_point(dark)
(7, 17)
>>> dark.x = 17.0
>>> dark.y = 7.0
>>> distance_between_points(blank, dark)
13.0
>>> class Rectangle(object):
...     """Represnts a rectanble.
... 
...     attributes: width, height, corner.
...     """
... 
>>> print Rectanble
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Rectanble' is not defined
>>> print Rectangle
<class '__main__.Rectangle'>
>>> bos = Rectangle()
>>> box = bos
>>> print box
<__main__.Rectangle object at 0x0000000009875240>
>>> box.w = 100.0
>>> box.h = 200.0
>>> box.c = Point()
>>> box.c = blank
>>> print box.c.x
5.0
>>> def find_center(rect):
...     p = Point()
...     p.x = rect.c.x + rect.w/2.0
...     p.y = rect.c.y + rect.h/2.0
...     return p
... 
>>> print find_center(box)
<__main__.Point object at 0x0000000009875278>
>>> find_center(box)
<__main__.Point object at 0x00000000098752E8>
>>> center.box = find_center(box)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'center' is not defined
>>> center_box = find_center(box)
>>> print_point(center)box)
  File "<stdin>", line 1
    print_point(center)box)
                         ^
SyntaxError: invalid syntax
>>> print_point(center_box)
(55, 112)
>>> def grow_rectangle(rect, dw, dh):
...     rect.w += dw
...     rect.h += dh
... 
>>> grow_rectabgle(box, -5.0, -12.0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'grow_rectabgle' is not defined
>>> grow_rectangle(box, -5.0, -12.0)
>>> center_box = find_center(box)
>>> print_point(center_box)
(52.5, 106)
>>> grow_rectangle(box, 5.0, 12.0)
>>> center_box = find_center(box)
>>> print_point(center_box)
(55, 112)
>>> def move_rectangle(rect, dx, dy):
...     rect.x += dx
...     rect.y += dy
... 
>>> move_rectangle(box, -5.0, -12.0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in move_rectangle
AttributeError: 'Rectangle' object has no attribute 'x'
>>> def move_rectangle(rect, dx, dy):
...     rect.c.x += dx
...     rect.c.y += dy
... 
>>> def move_rectangle(rect, dx, dy):
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block
>>> 
>>> move_rectangle(box, -5.0, -12.0)
>>> center_box = find_center(box)
>>> print_point(center_box)
(50, 100)
>>> class Point(object):
...     """Represents a point in 2-space."""
... 
>>> print Point
<class '__main__.Point'>
>>> WTF is Point
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'WTF' is not defined
>>> blank = Point()
>>> print blank
<__main__.Point object at 0x000000000210DE80>
>>> blank.x = 10.0
>>> blank.y = 12.0
>>> print blank
<__main__.Point object at 0x000000000210DE80>
>>> print '(%g, %g)' % (blank.x, blank.y)
(10, 12)
>>> distance = math.sqrt(blank.x**2 + blank.y**2)
>>> print distance
15.6204993518
>>> blank.x = 5.0
>>> blank.y = 12.0
>>> distance
15.620499351813308
>>> distance = math.sqrt(blank.x**2 + blank.y**2)
>>> distance
13.0
>>> print_point(blank)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print_point' is not defined
>>> print_Point(blnak)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print_Point' is not defined
>>> def print_point(p):
...     print '(%g, %g)' % (p.x, p.y)
... 
>>> print_point(blank)
(5, 12)
>>> def distance_between_points(p,q):
...     x1 = p.x
...     x2 = q.x
...     y1 = p.y
...     y2 = q.y
...     dx = x2 - x1
...     dy = y2 - y1
...     sq = dx**2 + dy**2
...     distance = math.sqrt(sq)
...     print distance
... 
>>> dark = Point()
>>> print dark
<__main__.Point object at 0x0000000009875198>
>>> dark.x = 7.0
>>> dark.y = 17.0
>>> distance_between_points(blank, dark)
5.38516480713
>>> print_point(blank)
(5, 12)
>>> print_point(dark)
(7, 17)
>>> dark.x = 17.0
>>> dark.y = 7.0
>>> distance_between_points(blank, dark)
13.0
>>> class Rectangle(object):
...     """Represnts a rectanble.
... 
...     attributes: width, height, corner.
...     """
... 
>>> print Rectanble
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Rectanble' is not defined
>>> print Rectangle
<class '__main__.Rectangle'>
>>> bos = Rectangle()
>>> box = bos
>>> print box
<__main__.Rectangle object at 0x0000000009875240>
>>> box.w = 100.0
>>> box.h = 200.0
>>> box.c = Point()
>>> box.c = blank
>>> print box.c.x
5.0
>>> def find_center(rect):
...     p = Point()
...     p.x = rect.c.x + rect.w/2.0
...     p.y = rect.c.y + rect.h/2.0
...     return p
... 
>>> print find_center(box)
<__main__.Point object at 0x0000000009875278>
>>> find_center(box)
<__main__.Point object at 0x00000000098752E8>
>>> center.box = find_center(box)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'center' is not defined
>>> center_box = find_center(box)
>>> print_point(center)box)
  File "<stdin>", line 1
    print_point(center)box)
                         ^
SyntaxError: invalid syntax
>>> print_point(center_box)
(55, 112)
>>> def grow_rectangle(rect, dw, dh):
...     rect.w += dw
...     rect.h += dh
... 
>>> grow_rectabgle(box, -5.0, -12.0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'grow_rectabgle' is not defined
>>> grow_rectangle(box, -5.0, -12.0)
>>> center_box = find_center(box)
>>> print_point(center_box)
(52.5, 106)
>>> grow_rectangle(box, 5.0, 12.0)
>>> center_box = find_center(box)
>>> print_point(center_box)
(55, 112)
>>> def move_rectangle(rect, dx, dy):
...     rect.x += dx
...     rect.y += dy
... 
>>> move_rectangle(box, -5.0, -12.0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in move_rectangle
AttributeError: 'Rectangle' object has no attribute 'x'
>>> def move_rectangle(rect, dx, dy):
...     rect.c.x += dx
...     rect.c.y += dy
... 
>>> def move_rectangle(rect, dx, dy):
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block
>>> 
>>> move_rectangle(box, -5.0, -12.0)
>>> center_box = find_center(box)
>>> print_point(center_box)
(50, 100)
>>> 