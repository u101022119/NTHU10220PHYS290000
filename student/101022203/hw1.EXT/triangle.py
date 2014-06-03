Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
import math
def is_triangle(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    s=[a,b,c]
    s.sort()
    [x,y,z]=s
    t=y-z
    r=y+z
    if z>t and z<r:
        print 'Yes, they form a triangle.'
    else :
        print "No, they don't form a triangle."
    
    
a=input('"a" stick length=')
b=input('"b" stick length=')
c=input('"c" stick length=')
is_triangle(a,b,c)
