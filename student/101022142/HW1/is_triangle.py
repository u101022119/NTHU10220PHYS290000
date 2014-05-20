#7.is_triangle.py
def is_triangle(a,b,c):
    if a+b<c:
        print'NO!This is not triangle!'
    if a+b>c:
        print'YES!This is a triangle!'

a=float(raw_input('give me a lenth of side a :'))
b=float(raw_input('give me a lenth of side b :'))
c=float(raw_input('give me a lenth of side c :'))

is_triangle(a,b,c)
