def is_triangle(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a+b<=c or a+c<=b or b+c<=a:
        print 'No'
    else:print 'Yes'
    return

is_triangle(1,1,1) ##T
is_triangle(1.4,1.4,2) ##F
is_triangle(1,2,2) ##T
is_triangle(3,4,5) ##T
