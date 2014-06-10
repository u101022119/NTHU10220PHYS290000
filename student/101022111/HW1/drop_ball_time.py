h = float( raw_input("How high is the tower: "))
t = float( raw_input("Enter the time interval: ") )
g = 9.81
s = 0.5*g*t**2
print "The height of the ball is ", h-s, "meters"
