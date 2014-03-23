def is_triangle():
    print 'this is a program that can check the three stick lengths you input that can form a triangle or not\n',
    print 'Let`s enter the stick lengths !!!\n',
    x = float(raw_input('the first stick = '))
    print('\n'),
    y = float(raw_input('the second stick = '))
    print('\n'),
    z = float(raw_input('the third stick = '))
    print('\n'),
    
    t=[x,y,z]
    t.sort()
    x = t.pop(2)
    y = t.pop(1)
    z = t.pop(0)
        
    w = y+z 
    a =(y**2+z**2)**(0.5) 
    if w <= x:
        print 'the three stick you enter cannot make a triangle SORRY~~~~'
    else :
        if y==z :
            if x!=y:
                if a<x :
                    print 'This is a isosceles obtuse triangle with three length(',x,',',y,',',z,')'
                if a==x :
                    print 'This is a isosceles right triangle with three length(',x,',',y,',',z,')'
                if a>x :
                    print 'This is a isosceles acute triangle with three length(',x,',',y,',',z,')'
            else :
                print 'This is a equilateral triangle with three length(',x,',',y,',',z,')'
        else :
            if a<x :
                print 'This is a obtuse triangle with three length(',x,',',y,',',z,')'
            if a==x :
                print 'This is a right triangle with three length(',x,',',y,',',z,')'
            if a>x :
                print 'This is a acute triangle with three length(',x,',',y,',',z,')'
is_triangle()
        
        
            
        
        
        
            
            
        
        
