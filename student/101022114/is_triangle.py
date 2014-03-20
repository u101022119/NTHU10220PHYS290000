def is_triangle(x,y,z):
    x=int(x)
    y=int(y)
    z=int(z)
    if x+y<=z or x+z<=y or y+z<=x:
        print'No'
    else:
        print'Yes'
