import math
a=float(raw_input('Put one length here. '))
b=float(raw_input('Put another length here. '))
c=float(raw_input('Put the last length here. '))
if a+b>c:
    if math.fabs(a-b)<c :
        print 'It can form a triangle.'
    else:
        print'It cannot form a triangle.'    
elif a+c>b:
    if math.fabs(a-c)<b:
        print 'It can form a triangle.'
    else:
        print'It cannot form a triangle.'   
elif b+c>a:
    if math.fabs(c-b)<a:
        print 'It can form a triangle.'
    else:
        print'It cannot form a triangle.'    
else:
    print'It cannot form a triangle.'
    


