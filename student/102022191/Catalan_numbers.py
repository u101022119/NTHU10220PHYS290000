N = 1000000000

cn =1
n=0
while cn < N:
    print cn
    cn  = cn * (4*n+2)/(n+2)
    n += 1
