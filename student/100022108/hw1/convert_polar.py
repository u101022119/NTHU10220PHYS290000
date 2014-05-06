def is_triangle(x,y,z):
    a=[x,y,z]
    sorted(a)
    if sorted(a)[0]+sorted(a)[1] > sorted(a)[2]:
        print 'yes'
    else:
        print 'no'
