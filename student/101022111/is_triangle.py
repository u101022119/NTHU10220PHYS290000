a=float(raw_input('What is your a side length:'))
b=float(raw_input('What is your b side length:'))
c=float(raw_input('What is your c side length:'))
def is_triangle(x,y,z):
    if x+y>z and z+y>x and x+z>y: 
        print 'YES!!'
    else:
        print 'NO!!!'
is_triangle(a,b,c)
