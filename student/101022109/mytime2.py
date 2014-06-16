class Time(object):
    def __cmp__(self,other):
        if self.h > other.h:
            print 'Time1 surpass Time2'
            return 1 
        elif self.h < other.h:
            print 'Time2 surpass Time1'
            return -1
        else:
            if self.m > other.m:
                print 'Time1 surpass Time2'
                return 1
            elif self.m < other.m:
                print 'Time2 surpass Time1'
                return -1
            else:
                if self.s > other.s:
                    print 'Time1 surpass Time2'
                    return 1
                elif self.s < other.s:
                    print 'Time2 surpass Time1'
                    return -1
                else:
                    print 'Time1 = Time2'
                    return 0

Time1 = Time()
Time2 = Time()


Time1.h = 2
Time1.m = 20
Time1.s = 23
Time2.h = 2
Time2.m = 20
Time2.s = 23

cmp(Time1,Time2)

Time1.h = 3
Time1.m = 25
Time1.s = 23
Time2.h = 2
Time2.m = 24
Time2.s = 23

cmp(Time1,Time2)


