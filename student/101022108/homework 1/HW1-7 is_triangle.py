import math
def is_triangle(x,y,z):
    if x+y>z and y+z>x and x+z>y :
        print 'Yes'
    else:
        print 'No'

print 'Input three lengths: '
x=float(raw_input())
y=float(raw_input())
z=float(raw_input())

is_triangle(x,y,z)
