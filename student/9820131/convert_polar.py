import math
x=float(raw_input('x='))
y=float(raw_input('y='))
def convert_polar(x,y):
    angle=math.asin(y/(x**2+y**2)**0.5)*360/(2*math.pi)
    print angle
convert_polar(x,y)
