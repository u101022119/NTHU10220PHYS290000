import math
x =input("Enter x coordinate: ")
y =input("Nnter y coordinate: ")
r =(x**2+y**2)**0.5
theta =math.atan(y/x)
theta =math.degrees(theta)
print "r = ",r
print "theta = ",theta,"degrees"
