def catalan(n):
    if n==0:
        return 1
    else:
        return int((4*n-2)/(n+1.0)*catalan(n-1))

i=0
while catalan(i)<1000000000:
    print catalan(i)
    i+=1
