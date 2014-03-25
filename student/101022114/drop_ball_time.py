g=10.0
h=float(raw_input("Put the height of the tower: "))
def drop_ball_time(h):
    if h>0:
        t=(2*h/g)**0.5
        return t
    elif h==0:
        return 0
    else:
        return'Sorry, the height cannot be negative.'

print drop_ball_time(h)

