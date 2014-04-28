import math

h=float(raw_input('the height of the tower='))
print '(m)'

t=float(raw_input('time interval='))
print '(s)'


a=-1*4.9*t*t+h

if a>=0:
    print a
else:
    print 0

