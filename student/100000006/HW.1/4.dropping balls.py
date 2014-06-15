


def drop_ball_height(h,t):
    s=t**2/2*9.8
    L=h-s
    if L>0:
        print 'still has',L,'m'
    else:
        print 'it had hit the ground'
h=float(raw_input("enter the heitht(m) of the tower:"))
t=float(raw_input("enter the time(s) after it is dropped:"))
drop_ball_height(h,t)
