def right_justify(s):
    i=0
    while i<(70-len(s)):
        print ' ',
        i=i+1
    print s

right_justify('apple')
