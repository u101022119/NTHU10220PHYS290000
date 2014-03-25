import math

print 'Enter the Cartesian coordinates x,y of a point in 2D space,'
print 'and I will transform it into polar coordinates.'

x=input('x:')
y=input('y:')

r = math.sqrt(x*x+y*y)
rad=math.acos(x/r)
deg=math.degrees(rad)

print '(',x,',',y,')','in polar coordinates is r =',r,'theta =',deg,
