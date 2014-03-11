#EX2: Right justify
#stu id: 101022171

from __future__ import print_function

def right_justify(s):
    i = 0  
    while i < (70-len(s)):
        print (' ',end='')
        i += 1
    print (s)

while True:
    x = raw_input("Input a string, end with 0: ")
    if x == '0':
        break
    right_justify(x)
