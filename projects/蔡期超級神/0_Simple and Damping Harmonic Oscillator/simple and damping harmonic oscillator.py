# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 16:27:00 2014

@author: user
"""

from pylab import*
from math import*
print 'Simple/Damping Harmonic Oscillator'
x0=float((raw_input("enter x0: ")))
v0=float((raw_input("enter v0: ")))
b=float((raw_input("enter b: ")))
w=float((raw_input("enter w: ")))
t=0 #initial time
h=0.01 #time step size
xdat=[]
vdat=[]#velocity data store here
time=[]#time stored here

v0=v0+h*(-w*w*x0-b*v0)/2

while(t<=50):
   
    x1=x0+h*v0
    v1=v0+h*(-w*w*x1-b*v0)
   
    xdat.append(x1)
    vdat.append(v1)
    time.append(t)
    x0=x1
    v0=v1
    t=t+h
   
figure(1)
title("Damped harmonic oscillator motion")
xlabel(" Time")
ylabel("x")
plot(time,xdat)
grid(True)
figure(2)
title("Damped harmonic oscillator motion")
xlabel("Time")
ylabel("Velocity")
plot(time,vdat)
grid(True)
figure(3)
title("Damped harmonic oscillator motion")
xlabel("x")
ylabel("velocity")
plot(xdat,vdat)
grid(True)

show()
