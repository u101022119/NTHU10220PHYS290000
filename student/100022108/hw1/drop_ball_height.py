def drop_ball_height():
    h = float(raw_input("Enter the height of the tower: "))
    t = float(raw_input("Enter the time interval:" ))
    s = 9.81*t**2/2.0
    print "the height of the ball is ", h-s, "meters"

