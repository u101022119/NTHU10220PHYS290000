def fibonacci_rec(n):
    if n<=0 or n!=int(n):
        return "Error!!"
    if n==1 or n==2:
        return 1
    else:return fibonacci_rec(n-1)+fibonacci_rec(n-2)

print "index  value "

for i in range(9):
    print i+1,"    ",fibonacci_rec(i+1)
