import math

def the_height(h,t):  
    g=9.8            #加速度         
    a=t**2
    s=g*a/2          #小球位移
    H=h-s
    b=2(H+s)/g
    c=math.sqrt(b)   #從高度h下落到地板所花時間
    print"enter h the height of tower,then after t time,the height of the ball is"
    return H
    print"the time the ball takes until it hits the ground is"
    return c
    
