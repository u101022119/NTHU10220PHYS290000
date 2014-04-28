def is_triangle(a,b,c):
    if (a+b)>c and(a+c)>b and(b+c)>a:
        print 'Yes'
    else:
        print 'No'

x=float(raw_input('x='))
y=float(raw_input('y='))
z=float(raw_input('z='))

is_triangle(int(x),int(y),int(z))
