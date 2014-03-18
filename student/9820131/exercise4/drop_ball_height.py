
def drop_ball_height(t,h):
   
    if h>0.5*9.8*(t**2):
        print 'The height of the ball='+(h-0.5*9.8*(t**2))
    else:
        print 'The height of the ball=0'
h=float(raw_input('h(in meters)='))
t=float(raw_input('t(in seconds)='))
drop_ball_height(t,h)

