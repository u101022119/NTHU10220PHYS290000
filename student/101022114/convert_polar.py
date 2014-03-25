import math
x=float(raw_input("Put the x in Cartesian: "))
y=float(raw_input("Put the y in Cartesian: "))
def convert_polar(x,y):
    r=(x**2+y**2)**(0.5)
    theta=math.atan(y/x)
    return(r,theta)
print convert_polar(x,y)
