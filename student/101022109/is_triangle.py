import math
def is_triangle(a,b,c):
    if a+b>c and math.fabs(a-b)<c and a+c>b and math.fabs(a-c)<b and b+c>a and math.fabs(b-c)<a:
        return 'True~~~'
    else:
        return 'Nope!!!'
a=raw_input('I need a stick length!!\n')
a=int(a)
b=raw_input('I need another!!\n')
b=int(b)
c=raw_input('I need the other!!\n')
c=int(c)

print is_triangle(a,b,c)


        
