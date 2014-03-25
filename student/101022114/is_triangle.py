x=float(raw_input("Put the length of one stick: "))
y=float(raw_input("Put another one: "))
z=float(raw_input("Put the other one: "))
def is_triangle(x,y,z):
    x=int(x)
    y=int(y)
    z=int(z)
    if x+y<=z or x+z<=y or y+z<=x:
        return False 
    else:
        return True

print is_triangle(x,y,z)


