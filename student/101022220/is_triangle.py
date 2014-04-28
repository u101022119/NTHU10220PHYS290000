def is_triangle(a, b, c):
    if a + b > c and c + a > b and b + c > a:
        print 'Yes'
    else:
        print 'No'

x = float(raw_input('the length of the first stick is(in meters):'))
y = float(raw_input('the length of the second stick is(in meters):'))
z = float(raw_input('the length of the third stick is(in meters):'))

is_triangle(x, y, z)

