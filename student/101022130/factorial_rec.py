def factorial_rec(n):
    if n<0:
        print 'factorial function is for positive numbers'
        return None
    elif n-int(n)!=0:
        print 'factorial function is for integers'
        return None
    else:
        if n==0:
            return 1
        else:
            value=n*factorial_rec(n-1)
            return value

print "f(5)\n", factorial_rec(5)
print "f(-5)\n", factorial_rec(-5)
print "f(4.5)\n", factorial_rec(4.5)
