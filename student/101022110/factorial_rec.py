def factorial_rec(n):
    if n<0:
        return 'factorial function is not for negative numbers'
    elif n-int(n)!=0:
        return 'factorial function is for integers'
    else:
        if n==0:
            return 1
        else:
            result=n*factorial_rec(n-1)
            return result

print "f(6)\n", factorial_rec(6)
print "f(-2)\n", factorial_rec(-2)
print "f(3.3)\n", factorial_rec(3.3)
