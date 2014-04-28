
import math
x = float( raw_input("Enter the x componant: ") )
y = float( raw_input("Enter the y componant: ") )
a = x**2
b = y**2
r = math.sqrt(a+b)
c = x/r
d = math.degrees(math.acos(c))
print "the corresponding polar coodinates r =", r," degrees =", d
