#File: drop_ball_time.py
#HW1_EX4_Dropping balls
#Due: 3/25/2014
#Author: 101022171

import math

h = input('Enter the height of the tower in meters >:')
t = input('Enter a time interval in seconds >:')

print "The ball above the ground after", t, "second(s) is", h-(0.5*9.8*(t**2)), "meter(s)."
print "The ball will hit the ground after %.4f second(s)." % (math.sqrt(2*h*9.8))
