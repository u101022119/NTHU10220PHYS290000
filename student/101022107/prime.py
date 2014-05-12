import math
prime=[2]
n=3
while n<=10000:
    t = 1
    while t<=math.sqrt(n):
        if n%(t+1)==0:
            t=t+1
            break
        elif  t == int(math.sqrt(n)):
            prime.append(n)
        t=t+1

    n = n+1
        
print prime   

        
        
    
        


           
            
        
            
            

   

    
    
