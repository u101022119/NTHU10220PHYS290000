#Nonlinear oscillator
#dx/dt=v
#dv/dt=-w*w*x-b*v
#Feynman Newton algorithm
from pylab import*
from math import*
x0=float(raw_input("Please enter the initial position x0: "))
v0=float(raw_input("Please enter the initial position v0: "))
w=float(raw_input("Please enter the frequency of the force w: "))
F=float(raw_input("Please enter the force F: "))
Q=float(raw_input("Please enter the damping factor Q: "))
t=0 #initial time
h=0.001 #time step size
T=1000

xdat=[]
vdat=[]#velocity data store here
time=[]#time stored here

v0=v0+h*(-x0-v0/Q)/2

while(t<=T-200):
   
    x1=x0+h*v0
    v1=v0+h*(-x1**3+x1-v0/Q+F*math.cos(w*t))
   
    x0=x1
    v0=v1
    t=t+h

while(t<=T):
   
    x1=x0+h*v0
    v1=v0+h*(-x1**3+x1-v0/Q+F*math.cos(w*t))
   
    xdat.append(x1)
    vdat.append(v1)
    time.append(t)
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
title("phase diagram")
xlabel("x")
ylabel("velocity")
plot(xdat,vdat)
grid(True)

show()
print "(%g,%g)" % (xdat[T],vdat[T])
