def is_triangle(a,b,c):
    if a+b>c:
        if a-b<c:
            print 'Yes!'
        else:
            print 'No!'
    else:
        print 'No!'

print 'This program is to help you check whether the sticks with given lenghs can form a triangle.'
x=input('Lengh_1:')
y=input('Lengh_2:')
z=input('Lengh_3:')

is_triangle(x,y,z)




        
