def drop_ball_height():
    h1=float(raw_input("Put the height of the tower: "))
    t=float(raw_input("Put the time interval: "))
    h2=h1-0.5*9.8*t*t
    return h2

print drop_ball_height()
    
