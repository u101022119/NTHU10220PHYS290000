def drop_ball_height(h,t):
    s=t**2/2*9.8
    L=h-s
    print L
h=float(raw_input("enter the heitht of the tower:"))
t=float(raw_input("enter the time after it is dropped:"))
drop_ball_height(h,t)
