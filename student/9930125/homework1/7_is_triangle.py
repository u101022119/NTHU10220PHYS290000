import math
x, y, z = float(raw_input('ENTER THE VALUE OF THE X: ')), float(raw_input('ENTER THE VALUE OF THE Y: ')), float(raw_input('ENTER THE VALUE OF THE Z: '))
def is_triangle():
    if z >= x + y:
        print 'NO'
    elif x >= y + z:
        print 'NO'
    elif y >= x + z:
        print 'NO'
    elif x <= math.fabs(y-z):
        print 'NO'
    elif y <= math.fabs(x-z):
        print 'NO'
    elif z <= math.fabs(x-y):
        print 'NO'
    else:
        print 'YES'

is_triangle()
