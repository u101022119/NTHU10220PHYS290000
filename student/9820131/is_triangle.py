import math
x = float( raw_input("Enter x: ") )
y = float( raw_input("Enter y: ") )
z = float( raw_input("Enter z: ") )
def is_triangle(x,y,z):
    if math.fabs(x+y)>math.fabs(z):
        if math.fabs(z+y)>math.fabs(x):
            if math.fabs(x+z)>math.fabs(y):
                print'yes'
                return
            return
        return
    print'no'
is_triangle(x,y,z)
    
