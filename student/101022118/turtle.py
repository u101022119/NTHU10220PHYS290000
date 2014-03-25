from swampy.TurtleWorld import *
import math


world = TurtleWorld()
wtf = Turtle()
print wtf


def square(t):
    for i in range(t):
        fd(wtf, 100)
        lt(wtf)

def polygon(n, l):
    wtf.delay = 0.00001
    theta = 360.0/n
    for i in range(n):
        fd(wtf, l)
        lt(wtf, theta)

def polygon1(theta, n, l):
    wtf.delay = 0.00001
    the = theta/n
    for i in range(n):
        fd(wtf, l)
        lt(wtf, the)


def circle(r):
    n = 360
    c = 2.0 * math.pi * r / n
    l = c / n
    polygon(n, l)

def arc(r, theta):
    n = 360
    c = 2.0 * math.pi * r / n
    l = c / n
    polygon1(theta, n, l)

def part(n, l):
    theta = 360.0 / n
    beta = ( 180 - theta ) / 2
    ll = ( 2 * l**2 - 2 * l**2 * math.cos(theta * 2 * math.pi / 360.0) )**(1.0/2)
    fd(wtf, ll)
    lt(wtf, 180.0 - beta)
    fd(wtf, l)
    lt(wtf, 180)
    fd(wtf, l)
    lt(wtf, 180.0 - beta)

def polygon2(n, l):
    wtf.delay=0.01
    nn = n
    while n > 0 :
        part(nn, l)
        n = n - 1


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2 :
        c = f(n-1) + f(n-2)
        return c



def center():
    fd(wtf, 800)
    rt(wtf)
    fd(wtf, 400)
    lt(wtf)

def F(l):
    ll = l*100
    rt(wtf)
    fd(wtf, 2*ll)
    lt(wtf, 180)
    fd(wtf, ll)
    rt(wtf)
    fd(wtf, ll)
    rt(wtf, 180)
    fd(wtf, ll)
    rt(wtf)
    fd(wtf, ll)
    rt(wtf)
    fd(wtf, ll)
    rt(wtf)
    
def W(l):
    ll = l*200
    rt(wtf, 75)
    fd(wtf, ll)
    lt(wtf, 150)
    fd(wtf, ll)
    rt(wtf, 150)
    fd(wtf, ll)
    lt(wtf, 150)
    fd(wtf, ll)
    rt(wtf, 75)

def T(l):
    ll = l*100
    fd(wtf, ll)
    rt(wtf)
    fd(wtf, 2*ll)
    lt(wtf, 180)
    fd(wtf, 2*ll)
    rt(wtf)
    fd(wtf, ll)

def WTF(l):
    W(l)
    T(l)
    F(l)

def F(n):
    while n > 0:
        print f(n),
        n = n-1
rt(wtf)
fd(wtf, 300)
polygon2(100, 400)
wait_for_user()

