def catalan_number(n):
    if n==0:
        return 1
    else:
        return int((4*n-2)/(n+1)*catalan_number(n-1))
k=0
while catalan_number(k)<1000000000:
    print catalan_number(k)
    k+=1
