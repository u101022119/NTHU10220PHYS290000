def Catalan_number(n):
    if n==0:
        return 1
    else:
        return (4*(n-1)+2)*(Catalan_number(n-1))/(n-1+2)


a=0
while Catalan_number(a)<1000000000:
    print Catalan_number(a)
    a+=1
