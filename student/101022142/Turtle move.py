from swampy.TurtleWorld import *
world = TurtleWorld()

tob=Turtle()
Bob = []  #Bob is a list of Turtle()
def bob():  #creat a lot of bob!
    t= int( input("how much bob do you want to use?") )
    for i in range( t ):
        Bob.append( Turtle() )
        Bob[i].pu()
        fd(Bob[i],50*i)
        print Bob[ i ]
        Bob[i].pd()
    return Bob
    
def polygon_usercall(t): #advance polygon with User interact !
    n= int( input("How many silde you want to draw?") )
    length=input("Give me silde length ")
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
    lt(t, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
    
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
    fd(t, step_length)
    lt(t, step_angle)
    
wait_for_user()
