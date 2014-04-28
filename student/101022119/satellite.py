import  math
def a(t):
    h=(6.67*10**-11*5.97*10**24*t**2/4.0/math.pi**2)**(1.0/3)-6417000
    print h ,'meters'
t=float(raw_input('enter the period(second) you want:'))
a(t)
