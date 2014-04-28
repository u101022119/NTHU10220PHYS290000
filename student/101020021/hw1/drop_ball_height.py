
h=float(raw_input('enter the height of tower :'))
t=float(raw_input('and enter the time interval :'))

def heigh(h,t):
  s=h-9.8*(t**2)/2
  if h-9.8*(t**2)/2<0:
    s=0
  return s


print 'after time t the height is :',heigh(h,t)
