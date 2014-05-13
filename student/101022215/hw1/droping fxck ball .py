g = 9.8
h=float(raw_input("Enter the initial height(m) you'd like it to be."))
t=float(raw_input("Enter the interval(s) you'd like it to be."))
def drop_ball_height(h,t):
    x = 0.5*g*(t**2)
    s = h-x
    if s>0:
        print 'At t seconds later, it will fall to the height of',h2,'above ground.'
    else:
        t2=(h/4.9)**(0.5)
        print 'It hit the fxckin ground', t-t2, 'seconds earlier.'
    
drop_ball_height(h,t)    
