h = float(raw_input('Input the height of tower\n'))
t = float(raw_input('Input the time interval\n'))
g = 9.8
position = h-(g*t**2)/2
if position >= 0:
    print position

if position <0:
    print 0
