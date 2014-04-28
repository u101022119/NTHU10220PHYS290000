h=float(raw_input("Enter the initial height(m) you'd like it to be."))
t=float(raw_input("Enter the time interval(s) you'd like it to be."))
h2=h-4.9*t*t
if h2>0:
   print 'At t seconds later, it will fall to the height of',h2,'above ground.'
if h2==0:
    print 'At t seconds later, it just kisses the ground.'
else:
    t2=(h/4.9)**(0.5)
    print 'It hit the ground',t-t2,'seconds earlier.'

    

