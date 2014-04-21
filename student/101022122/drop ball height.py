
h=float(raw_input('what is the height of the tower:'))
t=float(raw_input('time interval of the falling:'))

h1=h-4.9*(t**2.0)
if h1>0:
    print 'the height of the ball is above the ground at',t,'is ',h1,'meter'
elif h1==0:
    print 'bingo!'
else:
    print 'the ball is on the ground'

