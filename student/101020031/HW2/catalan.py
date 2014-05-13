def catalan(n):
    if n<0 :
        return none
    if n==0 :
        return 1
    if n>0 :
        return (4*n+2)/(n+2.0)*catalan(n-1)

n=0

while 1:
    print "for n=",n,",Cn=",catalan(n)
    if catalan(n+1)>10**9:
        break
    n=n+1
