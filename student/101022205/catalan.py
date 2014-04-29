def Catalan(n):
    if n==0:
        return 1
    else:
        return (4*(n-1)+2)*(Catalan(n-1))/(n+1)
x=0
while Catalan(x)< 1000000000:
    print Catalan(x)
    x+=1
    
