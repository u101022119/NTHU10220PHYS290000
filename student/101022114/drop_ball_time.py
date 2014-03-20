g=10.0
def drop_ball_time(h):
    if h>0:
        t=(2*h/g)**0.5
        print t
    elif h==0:
        print 0
    else:
        print'Sorry, the height cannot be negative.'

