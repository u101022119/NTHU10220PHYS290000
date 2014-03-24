#File: right_justify.py
#HW1_EX2_Right_justify
#Due: 3/25/2014
#Author: 101022171
	
from __future__ import print_function
	
def right_justify(s):
    i = 0  
    while i < (70-len(s)):
        print (' ',end='')
        i += 1
    print (s)
	
while True:
    x = raw_input("Input a string. (input 0 to end this program): ")
    if x == '0':
        break
    right_justify(x)
