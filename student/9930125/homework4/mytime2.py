class Time(object):
    def __cmp__(self,other):
        if self.hour > other.hour:
            print 'Time1 is ahead Time2'
            return 1 
        elif self.hour < other.hour:
            print 'Time2 is ahead Time1'
            return -1
        else:
            if self.minute > other.minute:
                print 'Time1 is ahead Time2'
                return 1
            elif self.minute < other.minute:
                print 'Time2 is ahead Time1'
                return -1
            else:
                if self.second > other.second:
                    print 'Time1 is ahead Time2'
                    return 1
                elif self.second < other.second:
                    print 'Time2 is ahead Time1'
                    return -1
                else:
                    print 'Time1 = Time2'
                    return 0

Time1 = Time()
Time2 = Time()

Time1.hour = float(raw_input('Time1.hour: '))
Time1.minute = float(raw_input('Time1.minute: '))
Time1.second = float(raw_input('Time1.second: '))
Time2.hour = float(raw_input('Time2.hour: '))
Time2.minute = float(raw_input('Time2.minute: '))
Time2.second = float(raw_input('Time2.second: '))

cmp(Time1,Time2)
