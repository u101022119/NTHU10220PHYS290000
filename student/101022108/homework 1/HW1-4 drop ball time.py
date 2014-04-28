h = float(raw_input('Input the height of the tower.\n'))
g = 9.8
t = (2*h/g)**(1.0/2)
if h>=0:
    print t
if h<0:
    print 'The height of tower is not exist.'
    
