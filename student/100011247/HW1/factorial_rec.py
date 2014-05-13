while 1:
 n =input("Enter a positive integer n: ")
 if n<0 or n%1!=0:#exclude none positive integers
     print "None"
 else:#Calculate n!
     i=n
     ans=1#Set 0!=1
     while i>1:
         ans=ans*i
         i=i-1
     print "n!=",ans
