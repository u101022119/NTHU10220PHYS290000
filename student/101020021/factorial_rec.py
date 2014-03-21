def factorial_rec(a):
    if int(a)!=a:
        print 'plz enter a interger!'
        return None
    elif a<0:
        print 'plz enter a positive number!'
        return None
    elif a==0:
        return 1
    else:
        b=a*factorial_rec(a-1)
    return int(b)


print 'for n=10 : ',factorial_rec(10)
print '\nfor n=10.5 : ',factorial_rec(10.5)
print '\nfor n=-10 : ',factorial_rec(-10)
