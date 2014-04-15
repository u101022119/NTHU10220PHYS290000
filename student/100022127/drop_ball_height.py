h=int(raw_input('Enter the Height : '))
t=int(raw_input('Enter the Time Interval : '))
x=9.8/2*t**2


if x>h:
    print "The Height after",t," sec is : 0 ."
else:
    print "The Height after",t," sec is : ",h-x,"."
