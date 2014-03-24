import math

g=9.801#m/s^2

h=float(raw_input("Please input the height(in meter)\n"))
t=float(raw_input("Please input the time inveterval(in second)\n"))


t_ground = math.sqrt(2.0*h/g)#hit the ground
h_after=h-0.5*g*t**2

if t>t_ground:
    print "height:0 (m)"
else:
    print "height:" , h_after , "m"
