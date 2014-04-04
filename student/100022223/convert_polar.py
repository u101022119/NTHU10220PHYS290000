import math

def cartesian_coordinate():
    x=float(raw_input('x: '))
    y=float(raw_input('y: '))
    r = (x**2+y**2)**0.5
    angle = math.atan(y/x)  #似乎不能拿了表示直角 #因為tan為無限大

    print "polar_coordinate(",r,",",angle,")"

print cartesian_coordinate()
