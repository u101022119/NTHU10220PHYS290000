x = raw_input("請輸入x座標")
x = float(x)
y = raw_input("請輸入y座標")
y = float(y)

import math
r = math.sqrt(x**2+y**2)
a = math.atan(y/x)
print r
print a
