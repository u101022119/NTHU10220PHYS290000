import math
h = float( raw_input("Enter the height in meters: "))
g = 9.81
t = math.sqrt(2*h/g)
print "The time the ball takes until it hits the ground", t, "seconds"
