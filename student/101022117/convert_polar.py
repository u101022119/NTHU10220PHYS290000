import math
def convert_polar(x,y):
    x=float(x)
    y=float(y)
    X=math.hypot(x,y)
    Y=math.atan2(y,x)/math.pi
    print '(',X,",",Y,"pi)"
