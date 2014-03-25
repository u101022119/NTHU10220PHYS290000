a=raw_input('輸入最長邊:')
b=raw_input('輸入第二長邊:')
c=raw_input('輸入最短邊:')
a=float(a)
b=float(b)
c=float(c)
if a<b+c:
    print 'yes'
else:
    print 'no'
