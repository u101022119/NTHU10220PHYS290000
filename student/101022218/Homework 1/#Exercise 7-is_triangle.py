def is_triangle(a,b,c):
    if a+b<c:
        print "No"
    elif b+c<a:
        print "No"
    elif a+c<b:
        print "No"
    else :
        print"Yes"

l1=float(raw_input("one stick's length:"))
l2=float(raw_input("another stick's length:"))
l3=float(raw_input("the other stick's length:"))
print"whether they can form a triangle?"
is_triangle(l1,l2,l3)
