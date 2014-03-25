def is_trangle(a,b,c):
    if a+b<=c or a+c<=b or b+c<=a:
        print 'No'
    else:
        print 'Yes'
a = input('Please enter the long of your first stick:')
b = input('Please enter the long of your second stick:')
c = input('Please enter the long of your third stick:')
is_trangle(a,b,c)
