#1.catalan.py
def catalan(n):
    if n==0:
        return 1
    if type(n)==int and n>0:
        return (4*n-2)/(n+1)*catalan(n-1)
    else :
        print 'n should be 0 or positive number'
for n in range(50):
    if catalan(n)<1000000:
        print catalan(n)
    if catalan(n)>1000000:
        print 'now it is the limit,when n=',n
        break
#for loop can use in "list",but now our list is unkonwn,so you can "guess" the range
