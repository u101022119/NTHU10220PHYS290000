def madelung(t):
    a=0.0
    for y in range(t):
        y=y+1
        for x in range(t):
            x=x+1
            for z in range (t):
                z=z+1
                if (x+y+z)%2==0:
                    a=a+1.0/(x**2+y**2+z**2)**(0.5)
                else:
                    a=a-1.0/(x**2+y**2+z**2)**(0.5)
    a=a*8
    y=0.0
    b=0.0
    for x in range(t):
        x=x+1
        for z in range (t):
            z=z+1
            if (x+y+z)%2==0:
                b=b+1.0/(x**2+y**2+z**2)**(0.5)
            else:
                b=b-1.0/(x**2+y**2+z**2)**(0.5)
    b=b*12
    x=0
    y=0
    c=0.0
    for z in range(t):
        z=z+1
        if x%2==0:
            c=c+1.0/z
        else:
            c=c-1.0/z
    c=c*6
    d=a+b+c
    print d 


madelung(1000)
