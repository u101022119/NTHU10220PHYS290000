h= float(raw_input('Enter height(meter):'))

t= float(raw_input('Enter time interval(second):'))

def drop_ball_height(h,t):
    x= 4.6*t*t
    if h>=x:
        print h-x
    elif h<x:
        print 'invalid input'
    elif h<0:
        print 'invalid input'
    elif t<0:
        print 'invalid input'
    
print drop_ball_height(h,t)
