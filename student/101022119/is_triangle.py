print 'whether sticks can form a triangle?'
x=float(raw_input('x='))
y=float(raw_input('y='))
z=float(raw_input('z='))

if x+y>z and y+z>x and x+z>y:
    print 'yes'
else:
    print 'no'

