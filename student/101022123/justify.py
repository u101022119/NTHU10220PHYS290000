def right_justify(a):
    
    s=len(a)
    i=0
    while i <= (70-s):
        print ' ',
        i+=1
    print a

right_justify('apple')
