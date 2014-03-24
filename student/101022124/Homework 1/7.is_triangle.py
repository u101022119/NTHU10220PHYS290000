
def is_triangle():
    a = int( float( raw_input("Enter first stick's length: ") ) )
    b = int( float( raw_input("Enter second stick's length: ") ) )
    c = int( float( raw_input("Enter third stick's length: ") ) )
    if a+b>c and a+c>b and b+c>a:
        print "Yes"
        print "first =",a
        print "second =",b
        print "third =",c
    else:
        print "No"
        print "first =",a
        print "second =",b
        print "third =",c

is_triangle()
