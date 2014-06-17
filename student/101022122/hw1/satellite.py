t=input('enter the time interval of the satellite:')
import math
h=(((6.67*10**-11)*(5.97*10**24)*(t**2)/4/(math.pi**2))**(1.0/3))-6417
print 'the attitude of the staellite is',h,'meters'
