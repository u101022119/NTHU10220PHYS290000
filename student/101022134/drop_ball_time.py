#Homewrok 1 exercise 4
h = float(raw_input('the height of the tower is(in meters):'))
t = float(raw_input('the time that the ball drops is(in seconds):'))
g = 9.8
H = h - 1/2.0 * g * t**2

print 'the height of the ball at time', t, 'second(s) is', H, 'meters'
