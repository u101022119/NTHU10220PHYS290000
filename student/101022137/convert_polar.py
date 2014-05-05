import math
X=float(raw_input( 'Enter the number of X:' ))
Y=float (raw_input( 'Enter the number of Y:'))
r=(X*X+Y*Y)**0.5
theta=math.atan2(Y, X)*180/math.pi
print ' The value of r', r
print ' The value of theta', theta
