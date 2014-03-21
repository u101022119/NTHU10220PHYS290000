h=float(raw_input('the height of the tower (in meters) :'))
t=float(raw_input('the time interval (in seconds) :'))
s=h-(9.8*t**2)/2

if h<=0 or t<=0:
    print 'Both the height and the time have to be positive.'
elif s<=0:
    print 'The ball hits the ground.'
else:
    print 'The height of the ball above the ground is' , s , 'm'

