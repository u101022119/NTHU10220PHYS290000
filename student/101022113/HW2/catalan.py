def catalan(n):
    if n==0:
        return 1
    else:
        return (4*n-2)/(n+1)*catalan(n-1)
n=float(raw_input("Put n right here!"))
if n<=1000000000:
   print catalan(n) 
else:
    print "Your n is too big!"
