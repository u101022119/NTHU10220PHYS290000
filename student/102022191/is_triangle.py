def is_triangle(lis):
    lis.sort()
    if lis[0] + lis[1] > lis[2]:
        return True
    return False

lis = [0]*3
print ("Please input 3 integers")
for i in range(3):
    lis[i] = int(raw_input())

if is_triangle(lis):
    print ("Yes")
else:
    print ("No")
