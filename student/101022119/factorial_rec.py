n=input('n=')
def a(n,t):
    if not isinstance(n,int):
        print 'Factorial is only defined for integers.'
        print None
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        print None
    elif 0==n%1 and n >0:
        t=t*n
        n=n-1
        if n>0:            
            a(n,t)
        else:
            print t
            
    elif n==0:
        print  '1'
    


a(n,1)
