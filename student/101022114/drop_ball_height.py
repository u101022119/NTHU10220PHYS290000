g=10.0
def drop_ball_height(h,t):
    if h>(0.5*g*(t**2)):
        h=h-(0.5*g*(t**2))
        print h
    elif h<0:
        print'Sorry, the height cannot be negative.'
    elif t<0:
        print'Sorry, the time cannot be negative.'
    else:
        print 0

    
