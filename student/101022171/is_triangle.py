#File: is_triangle.py
#HW1_EX7_ Is_trangle?
#Due: 3/25/2014
#Author: 101022171

def is_triangle(a, b ,c):
    if (a + b) <= c :
        print ("NO, canoot form a triangle.")
    elif (a + c) <= b:
        print ("NO, canoot form a triangle.")
    elif (b + c) < a:
        print ("NO, canoot form a triangle.")
    else: print ("Yes, can form a triangle.")

    
a = int (input("Enter an integer a >:"))
b = int (input("Enter an integer b >:"))
c = int (input("Enter an integer c >:"))

is_triangle(a, b, c)
