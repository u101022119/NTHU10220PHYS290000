def fibonacci_rec(a):
    if int(a)!=a:
        print 'fibonacci is for intergers'
        return None
    elif a<0:
        print 'fibonacci is for positive numbers'
        return None
    elif a==0:
        return 0
    elif a==1:
        return 1    
    else:
        b=fibonacci_rec(a-1)+fibonacci_rec(a-2)
    return int(b)


print 'for n=8 : ',fibonacci_rec(8)
print 'for n=7.5 : ',fibonacci_rec(7.5)
print 'for n=-8 : ',fibonacci_rec(-8)
print 'for n=9 : ',fibonacci_rec(9)
