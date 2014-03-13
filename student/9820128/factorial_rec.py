def factorial_rec(x):
    if x>0 and x-int(x) == 0:
        s=factorial_rec(x-1)
        t=s*x
        return t
    elif x==0:
        return 1
    else:
        return 'None'


s1=5
s2=0
s3=-2
s4=2.4
print 'factorial_rec(s1) is', factorial_rec(s1)
print 'factorial_rec(s2) is', factorial_rec(s2)
print 'factorial_rec(s3) is', factorial_rec(s3)
print 'factorial_rec(s4) is', factorial_rec(s4)
