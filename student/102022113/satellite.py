import math

T=float(raw_input('The period T (in seconds) = '))

if T<=0:
    print 'The period has to be positive.'
else:
    G=6.67e-11
    M=5.97e24
    R=6417e3

    x=G*M*T**2
    y=4*math.pi**2

    h=math.pow((x/y),(1.0/3.0))-R

    if h<=0:
        print 'The period is too small.'
    else:
        print 'The attitude h above the Earth’s surface is', h, 'meters.'
