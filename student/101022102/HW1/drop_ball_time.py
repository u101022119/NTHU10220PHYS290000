H = raw_input("請輸入塔的高度")
H = float(H)

h = raw_input("請輸入所求高度")
h = float(h)

import math

if h <= H:
    t = math.sqrt((H-h)/(0.5*9.8))
    T = math.sqrt(H/(0.5*9.8))
    print T-t
    
