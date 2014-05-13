while 1:
 a= input("Enter the lengh of three sticks :")
 b= input("Enter the lengh of three sticks :")
 c= input("Enter the lengh of three sticks :")

 if a+b>c and a+c>b and c+b>a:
    print "Yes,they can form a triangle\n"
 else:
    print "No,they can't form a triangle\n"
