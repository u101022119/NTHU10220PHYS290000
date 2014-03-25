import math
H=raw_input('input height:')
t=raw_input('input time:')
H=float(H)
t=float(t)
h=H-0.5*9.8*t**2
print h


x=raw_input('input tower height:')
y=raw_input('input window height:')
x=float(x)
y=float(y)
T=math.sqrt(2*(x-y)/9.8)
print 'the ball reach the window at' ,T

