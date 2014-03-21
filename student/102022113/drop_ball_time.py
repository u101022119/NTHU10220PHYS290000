import math

h=float(raw_input('the height of the tower (in meters) :'))

if h<0:
    print 'The hight cannot be negative.'
else:
    t=math.sqrt(2*h/9.8)
    print 'It takes' , t , 'seconds for the ball to hit the ground.'
