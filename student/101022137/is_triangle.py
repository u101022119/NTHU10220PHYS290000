import math
a,b,c=float(raw_input(' The value of a: ')),float(raw_input(' The value of b: ')),float(raw_input(' The value of c: '))
def is_triangle():
    if c>=a+b:
        print 'NO'
    elif a>=b+c:
        print 'NO'
    elif b>=a+c:
        print 'NO'
    elif c<=math.fabs(a-b):
        print 'NO'
    elif a<=maht.fabs(c-b):
        print 'NO'
    elif b<=math.fabs(a-c):
        print 'NO'
    else:
        print 'YES'
