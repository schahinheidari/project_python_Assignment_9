class Time:

    def __init__(self, h, m, s):   
        self.hour = h
        self.minute = m
        self.second = s

    def sum(self,mehman):
        result = Time(None,None,None)
        result.s = self.s + mehman.s
        result.m = self.m + mehman.m
        result.h = self.h + mehman.h
        if result.s > 59:
            result.s -=60
            result.m += 1
            if result.m >59:
                result.m -=60
                result.h +=1
        return result

    def sub(self, mehman):
        result = Time(None,None,None)
        if mehman.s > self.s:
            self.m -=1
            self.s +=60
        result.s = self.s - mehman.s
        if mehman.m > self.m:
                self.h -=1
                self.m +=60
        result.m = self.m - mehman.m
        result.h = self.h - mehman.h
        return result

    def timeToSecond(self):
        result = Time(None,None,None)
        result = (self.h * 3600) + (self.m * 60) + (self.s)
        return result
    
    def SecondToTime(self):
        result = Time(None,None,None)
        result.h = self.s // 3600
        result.m = (self.s % 3600) // 60
        result.s = (self.s % 3600) % 60
        return result 
    
    def show(self):
        print(self.h,":",self.m,":",self.s)