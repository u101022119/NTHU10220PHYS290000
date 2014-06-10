#Harmonic oscillator
#dx/dt=v
#dv/dt=-w*w*x
#x(t+h)=x(t)+h*v(t+h/2)
#v(t+h/2)=v(t-h/2)+h*a(t)
#v(1/2)=v0+(h/2)a0
from pylab import*
from math import*
x0=0.754682
v0=-59.7952
w=2
t=0 #initial time
h=0.001 #time step size

xdat=[]
vdat=[]#velocity data store here
time=[]#time stored here
v0=v0+h*(-w*w*x0)/2
while(t<=100):
    x1=x0+h*v0
    v1=v0+h*(-w*w*x1)
   
   
    xdat.append(x1)
    vdat.append(v1)
    time.append(t)
    x0=x1
    v0=v1
    t=t+h
   
figure(1)
title("Harmonic oscillator motion")
xlabel(" Time")
ylabel("x")
plot(time,xdat)
grid(True)

figure(2)
title("Harmonic oscillator motion")
xlabel("Time")
ylabel("Velocity")
plot(time,vdat)
grid(True)

figure(3)
title("Harmonic oscillator motion")
xlabel("x")
ylabel("Velocity")
plot(xdat,vdat)
grid(True)

show()
