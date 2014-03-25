import math
x=float(raw_input('enter the x coordinates'))
y=float(raw_input('enter the y coordinates'))
r=(x**2+y**2)**(0.5)
theta=math.asin(y/r)
print [r ,theta]
