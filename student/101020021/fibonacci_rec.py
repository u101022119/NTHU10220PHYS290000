def fibonacci_rec(a):
    if int(a)!=a:
        print 'plz enter a interger!'
        return None
    elif a<0:
        print 'plz enter a positive number!'
        return None
    elif a==0:
        return 0
    elif a==1:
        return 1    
    else:
        b=fibonacci_rec(a-1)+fibonacci_rec(a-2)
    return int(b)


print 'for n=10 : ',fibonacci_rec(10)
print '\nfor n=10.5 : ',fibonacci_rec(10.5)
print '\nfor n=-10 : ',fibonacci_rec(-10)
