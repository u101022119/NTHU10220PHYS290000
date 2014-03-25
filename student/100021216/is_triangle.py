import math

def is_triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print 'Yes'
    else:
        print 'No'

print 'Enter the three stick lengths(a,b,c) of a tringle(in integer)'
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

print 'Can these three stick form a tringle?'
is_triangle(a,b,c)
