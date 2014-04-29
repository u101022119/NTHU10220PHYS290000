def is_triangle(x,y,z):
    a=int(x)
    b=int(y)
    c=int(z)
    if a+b <= c :
        print "NO"
    elif b+c <= a:
        print "NO"
    elif a+c <= b:
        print "NO"
    else:
        print "YES"


is_triangle(3.5456,4.654,5.65465)      #YES
is_triangle(2.65465,6.54654,100.65465) #NO
 
