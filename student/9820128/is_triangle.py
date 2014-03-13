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
