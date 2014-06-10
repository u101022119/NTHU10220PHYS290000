while 1:
 n =input("Enter a positive integer n: ")
 if n<0 or n%1!=0:#exclude none positive integers
     print "None"
 else:#Calculate nth term of fibonacci series!
     i=n
     ans,a=1,1
     while i>2:
         b=ans
         ans=ans+a
         a=b
         i=i-1
     print n,"th term of fibonacci series is",ans
     
