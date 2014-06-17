# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 16:48:27 2014

@author: user
"""

#Driven harmonic oscillator
#dx/dt=v
#dv/dt=-w*w*x-b*v
from pylab import*
from math import*
x0=float(raw_input("Please enter the initial position x0: "))
v0=float(raw_input("Please enter the initial velocity v0: "))
w=float(raw_input("Please enter the frequency w of the force F: "))
F=float(raw_input("Please enter the force F: "))
Q=4
t=0 #initial time
h=0.001 #time step size
T=50 #time interval
N=T/h #data number

xdat=[]
vdat=[]#velocity data store here
time=[]#time stored here

v0=v0+h*(-x0-v0/Q)/2

while(t<=100):
   
    x1=x0+h*v0
    v1=v0+h*(-x1-v0/Q+F*math.cos(w*t))   
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
title("Phase diagram")
xlabel("x")
ylabel("velocity")
plot(xdat,vdat)
grid(True)

show()

print "(%g,%g)" % (xdat[T],vdat[T])
