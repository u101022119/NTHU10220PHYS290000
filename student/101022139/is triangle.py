x=float(raw_input('the length of the first sticks is: '))
y=float(raw_input('the length of the second sticks is: '))
z=float(raw_input('the length of the third sticks is: '))

if x<=0 or y<=0 or z<=0:
    print 'No,you cannot form a triangle , all the lengths have to be positive'

else:
    def is_triangle(x,y,z):
        if x+y>=z and y+z>=x and z+x>=y:
            print 'Yes , you can form a triangle from sticks with the tree given lenths'
        else:
            print 'No, you cannot form a triangle from sticks with the three given lengths'
    is_triangle(x,y,z)
    
