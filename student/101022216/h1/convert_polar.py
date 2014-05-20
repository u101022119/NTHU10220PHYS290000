imput math

x= float(raw_input('Enter coordinate x:'))

y= float(raw_input('Enter coordinate y:'))

def convert(x,y):
    r=(x**2+y**2)**(0.5)
    c= y/x
    theta= math.atan(c)
    print r
    print theta

convert(x,y)


    
