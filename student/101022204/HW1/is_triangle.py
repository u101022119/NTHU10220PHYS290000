a = float(raw_input('Enter the first stick length:'))
b = float(raw_input('Enter the second stick length:'))
c = float(raw_input('Enter the third stick length:'))

def is_triangle(a,b,c):
    if a+b > c and b+c > a and a+c > b:
        print 'Yes'   
    else:      
        print 'No'

is_triangle(a,b,c)
