
n=input('enter a number:')
def fa(n):
    if n<0:
        print 'factorial number cannot be negative'
    elif not isinstance(n,int):
        print 'factorial number need to be integer'
    elif n==0:
        return 1
    else:
        return n*fa(n-1)

x=fa(n)
if not isinstance(x,int):
    pass
else:
    print x
