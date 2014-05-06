import math
	
def cartesian_coordinate():
    x=float(raw_input('Put the x component: '))
    y=float(raw_input('Put the y component: '))
    R = (x*x+y*y)**0.5
    angle = math.atan(y/x)
	
    print "polar_coordinate(",R,",",angle,")"

cartesian_coordinate()
