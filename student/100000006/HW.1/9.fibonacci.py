

def fibonacci(n):
    if n<=0 or n!=int(n):
        return "Error!!"
    if n==1 or n==2:
        return 1
    else:return fibonacci(n-1)+fibonacci(n-2)

print "index  value "

for i in range(9):
    print i+1,"    ",fibonacci(i+1)
