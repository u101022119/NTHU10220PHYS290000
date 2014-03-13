def fibonacci_rec(x):

    if x==0:
        return 1
    elif x==1:
        return 1
    elif x>0 and x-int(x) == 0:
        s1=fibonacci_rec(x-1)
        s2=fibonacci_rec(x-2)
        t=s1+s2
        return t
    elif x==0:
        return 1
    else:
        return 'None'

s1=5
s2=0
s3=-2
s4=4.4

print "fibonacci_rec(s1) is", fibonacci_rec(s1)
print "fibonacci_rec(s2) is", fibonacci_rec(s2)
print "fibonacci_rec(s3) is", fibonacci_rec(s3)
print "fibonacci_rec(s4) is", fibonacci_rec(s4)



