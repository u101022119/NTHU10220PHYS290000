k=int(raw_input('what is your n:'))

def catalan(n):
    p=1
    a=0
    while n>a:
        p=(4*a+2)*p/(a+2)
        a=a+1
        print p
    return a,p

catalan(k)  
