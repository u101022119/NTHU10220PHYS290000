def catalan(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return catalan(n-1)*(4*n-2)/(n+1)

for n in range (1,19):
    print catalan(n)

