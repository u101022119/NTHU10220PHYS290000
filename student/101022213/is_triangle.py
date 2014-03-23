def is_triangle(x,y,z):
    n=0
    if x+y >z:
        n = n+1
    if x+z>y:
        n=n+1
    if y+z>x:
        n=n+1

    if n%3 ==0:
        print"Yes"
    else:
        print"No"
