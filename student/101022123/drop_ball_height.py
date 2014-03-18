def drop_ball_height():
    h=float(raw_input("Enter the height of the tower h plz\n"))
    print'\n',
    t=float(raw_input("Enter a time interval t plz\n"))
    print'\n',
    x = h - 4.9*t**2
    if x<0:
        print 'the ball is already on the gound !!!'
    else:    
        print "The height of the ball above the ground at time t after it is dropped is",x
drop_ball_height()
