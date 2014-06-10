def catalan(c):
    a,b=1,0
    t=20000000
    for i in range(t):
        a,b=(4.0*i+2)/(i+2)*a,a
        if b>c:
            break
            
        print b


catalan(1000000)
