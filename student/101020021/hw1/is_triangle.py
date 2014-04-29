def is_triangle(a,b,c):

    print 'after convert\nx = ',a,'\ny = ',b,'\nz = ',c,'\nIs trangle?'
    t=[a,b,c]
    t.sort()
    if t[0]+t[1]>t[2]:
      print 'Yes'
    else:
      print 'No'
    
print 'enter 3 stick lengths\nwe will convert them to integers'
x=int(float(raw_input('x = ')))
y=int(float(raw_input('y = ')))
z=int(float(raw_input('z = ')))

is_triangle(x,y,z)
