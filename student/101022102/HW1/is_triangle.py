a = raw_input("請輸入三角形最短邊")
a = float(a)
b = raw_input("請輸入三角形一邊長")
b = float(b)
c = raw_input("請輸入三角形最長邊")
c = float(c)

if a+b>c and b-a<c:
    print 'is_triangle'

