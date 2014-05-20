x=int(raw_input('what argument you want:'))
a=0
b=1
def identify(n):
    if type(n) != int or n < 0:
        print 'None'
    elif n == 0:
        print 0
    elif n == 1:
        print 1
    else:
        k=n
        global fibonacci_rec
        fibonacci_rec(k)

def fibonacci_rec(k):
    while k !=0:
        c=a+b
        print b
        a=b
        b=c
        k=k-1
        global a,b
        return fibonacci_rec(k),a,b,k
        if k==0:
            break
identify(x)
