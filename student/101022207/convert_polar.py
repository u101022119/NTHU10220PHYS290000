import math
def convert_polar():
    x=float(raw_input('Put the x component: '))
    y=float(raw_input('Put the y component: '))
    l=(x**2+y**2)**0.5
    r=math.asin(y/l)
    print '(' , l , r , ')'

convert_polar()
