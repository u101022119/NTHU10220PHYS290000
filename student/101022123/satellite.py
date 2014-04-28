import math
def satellite():
    print 'A satellite is to be launched into a circular orbit around the Earth\n',
    print 'so that it orbits the planet once every T seconds',
    T = float(raw_input('Please enter T ='))
    print('\n'),
    G = 6.67*(10**(-11))
    M = 5.97*(10**24)
    R = 6417*(10**3)
    x = G*M*(T**2)/4*(3.14**2)
    h = x**(0.3333333333333333333)-R
    if h > 0:
              print ' the attitude h above the Earth`s surface that the satellite is',h
    else :
              print ' the satellite is already on the ground~~'
satellite()

