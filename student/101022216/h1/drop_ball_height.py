
print 'If you drop the ball from the top of the tower at time t,'
print 'enter the heigh of the tower and time t,'
print 'and I will tell you the heigh of the ball above the ground at time t.'
height=input('Enter the height(m):')
time=input('Enter the time(s):')

if height <= 9.8*time*time/2:
    print 'The ball has been on the ground.'


else :
    height_ball=heigh-10*time*time/2
    print 'The ball is',height_ball,'meters above the ground.'
