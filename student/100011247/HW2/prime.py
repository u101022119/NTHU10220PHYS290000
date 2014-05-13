import math
Prime = [2]

def is_Prime(i,j):
	global c	
	if i%Prime[j]==0:
		c=1
	else:
		c=0
	return c

for i in range(3,10000):
	n=math.sqrt(i)//1
	for j in range(len(Prime)):
		is_Prime(i,j)
		if c==1:
			break			
		elif c==0:
			if n<=Prime[j]:
				Prime.append(i)
				break
			else:
	 		    continue
			
print Prime	

