g=10.0
h=float(raw_input("Put the height of the tower: "))
t=float(raw_input("Put the time interval: "))
def drop_ball_height(h,t):
    if h>(0.5*g*(t**2)):
        h=h-(0.5*g*(t**2))
        return h
    else:
        return 0

print drop_ball_height(h,t)


