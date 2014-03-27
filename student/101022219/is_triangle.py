x = float (raw_input('The length of the first side of the triangle: '))
y = float (raw_input('The length of the first side of the triangle: '))
z = float (raw_input('The length of the first side of the triangle: '))

def is_triangle(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        print 'Yes'
    else:
        print 'No'

is_triangle(x, y, z)
