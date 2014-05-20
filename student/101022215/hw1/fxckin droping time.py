g=9.8
h=float(raw_input("enter whatever you want."))
def drop_ball_time(h):
    t = (2*h/g)**(0.5)
    return t

print drop_ball_time(h)
