h=float(raw_input('the height of the tower (in meters) :'))
t=float(raw_input('the time interval (in seconds) :'))
s=h-(9.8*t**2)/2

print 'The height of the ball above the ground is' , s , 'm'
