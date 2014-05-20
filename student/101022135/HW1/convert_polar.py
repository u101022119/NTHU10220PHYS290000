#File: convert_polar.py
#HW1_EX5_Converting_polar_coordinates
#Due: 3/25/2014
#Author: 101022171


import math

def convert_polar(x, y):
     r = math.sqrt(x**2 + y**2)
     theta = math.acos(x/r)
    
     theta = math.degrees( theta )

     print "The polar coordinate corresponding to the Cartesian coordinate (%d, %d) is :" % (x, y)
     print "R = %.2f and angle(in degree) = %.2f" % (r, theta)


x = float( input("Enter the value of x >:") )
y = float( input("Enter the value of y >:") )

convert_polar(x, y)
