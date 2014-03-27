h = float( raw_input("Enter the height of the tower:"))
t = float( raw_input("Enter the time interval:"))
s = 9.8*t**2/2.0
print "The height of the ball is", h-s, "meters"
    
h = float( raw_input("Enter the peight of the tower:"))
t = (2*h/9.8)**0.5
print "The time interval it takes until hitting the ground", t, "meters"
