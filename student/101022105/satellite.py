import math
t=float(raw_input('Please enter the desired time period(hour) you want the satellite to orbit the Earth.'))
R=6417
G=6.67*10**(-11)
M=5.97*100
h=((G*M*(3600*t)**2/(4/(math.pi**2)))**(1.0/3))/1000-R
if h>0 or h==0:
   print 'Then, the satellite should be orbiting',h,"km above the Earth's surface in order to orbit the Earth in",t,'seconds.' 
else:
    print "Well, unfortunately, that's impossible.",h
