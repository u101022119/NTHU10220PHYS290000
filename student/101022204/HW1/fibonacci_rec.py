def fibonacci_rec(a):
    if int(a)!=a:
        print 'It must be an integer'
        return None
    elif a<0:
        print 'It can not be negative'
        return None
    elif a==0:
        return 0
    elif a==1:
        return 1    
    else:
        b=fibonacci_rec(a-1)+fibonacci_rec(a-2)
    return int(b)

print 'Enter a figure "a" for fibonacci_rec(a)'
