def is_triangle(a,b,c):
    if a+b>c or b+c>a or a+c>b:
        print "yes!"
    else :
        print "no!"
        
a = int( raw_input("Enter the length of the first stick: "))   
b = int( raw_input("Enter the length of the second stick: "))         
c = int( raw_input("Enter the length of the third stick: "))    
is_triangle(a,b,c)
