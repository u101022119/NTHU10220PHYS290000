from pylab import*
from math import*
x0=10
v0=0
w=math.pi
F=50
Q=0.05
t=0 #initial time
h=0.001 #time step size
T=500 #time interval
N=T/h #data number

xdat=[]
vdat=[]#velocity data store here
time=[]#time stored here
driven=[]
driven1=[]

v0=v0+h*(-x0-v0/Q)/2

while(t<=T-200):
   
    x1=x0+h*v0
    v1=v0+h*(-2*math.pi*x1-v0/Q+F*math.cos(w*t))
    x0=x1
    v0=v1
    t=t+h


while(t<=T):
   
    x1=x0+h*v0
    v1=v0+h*(-2*math.pi*x1-v0/Q+F*math.cos(w*t))    
    p=w*t
    a=math.cos(p)
   
    xdat.append(x1)
    vdat.append(v1)
    time.append(t)
    driven.append(a)
    x0=x1
    v0=v1
    t=t+h
   
   
figure(1)
title("x-t")
xlabel(" Time")
ylabel("x")
plot(time,xdat)
grid(True)
figure(2)
title("v-t")
xlabel("Time")
ylabel("Velocity")
plot(time,vdat)
grid(True)
figure(3)
title("Phase diagram")
xlabel("x")
ylabel("velocity")
plot(xdat,vdat)
grid(True)
figure(4)
title("Lissajous")
xlabel("x")
ylabel("F")
plot(xdat,driven)
grid(True)

show()

print "(%g,%g)" % (xdat[T],vdat[T])