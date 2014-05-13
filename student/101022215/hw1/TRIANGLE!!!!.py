a=float(raw_input('enter a integer plz!!!'))
b=float(raw_input('enter a integer plz!!!'))
c=float(raw_input('enter a integer plz!!!'))
def is_triangle(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    if a+b>c and a+c>b and b+c>a:
        print 'yes'
    else:
        print 'no'
is_triangle(a,b,c)
