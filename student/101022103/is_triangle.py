def is_triangle(a,b,c):
    if a>0 and b>0 and c>0:
        if a+b>c or a+c>b or b+c>a:
            print 'YES'
        else:
            print 'NO'
    else:
        print 'NO'


a= raw_input('Enter length a:')
b= raw_input('Enter length b:')
c= raw_input('Enter length c:')

def is_triangle(a,b,c):
    if a>0 and b>0 and c>0:
        if a+b>c or a+c>b or b+c>a:
            print 'YES'
        else:
            print 'NO'
    else:
        print 'NO'

is_triangle(a,b,c)

