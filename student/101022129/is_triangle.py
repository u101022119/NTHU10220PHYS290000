x = float(raw_input('Put the first stick length:'))
y = float(raw_input('Put the second stick length:'))
z = float(raw_input('Put the third stick length:'))

def is_triangle(a, b, c):    
    if a + b > c and c + a > b and b + c > a:
        print 'yes,it is a triangle'
    else:
        print 'No,it is not a triangle'

is_triangle(x, y, z)
