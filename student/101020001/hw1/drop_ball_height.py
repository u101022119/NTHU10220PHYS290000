h=input('Please enter the height:')
t=input('Please enter the time:')

s=h-4.9*t**2
if s<0:
    print 'the height of the ball above the ground is 0'
else :
    print 'the height of the ball above the ground',s
