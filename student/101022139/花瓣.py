import math
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay=10**-500000
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
for i in range(100):
    arc(bob, 100, 100)
    lt(bob,130)
wait_for_user()
