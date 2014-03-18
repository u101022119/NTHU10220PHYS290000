import math
def is_triangle(a, b, c):
    if a+b>c and math.fabs(a-b)<c and a+c>b and math.fabs(a-c)<b and b+c>a and math.fabs(b-c)<a:
        return 'Yes'
    else:
        return 'No'

print 'input three stick lengths'
a=raw_input()
b=raw_input()
c=raw_input()
a=int(a)
b=int(b)
c=int(c)

print is_triangle(a, b, c)
