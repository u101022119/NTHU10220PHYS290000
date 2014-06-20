class Time(object):
    def __cmp__(self,other):
        return self.hour*3600 + self.minute*60 + self.second > other.hour*3600 + other.minute*60 + other.second
        
time1 = Time()
time1.hour = 5
time1.minute = 40
time1.second = 6

time2 = Time()
time2.hour = 6
time2.minute = 52
time2.second = 3

print time1 > time2
print time2 > time1