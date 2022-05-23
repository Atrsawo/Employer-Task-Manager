import datetime
from tracemalloc import start

class Resource:
    def __init__(self,name,unAvailablityTime):
        self.name = name
        self.unAvailablityTime=unAvailablityTime
    
    def checkAvailable(self,startTime,endTime):
        for object in self.unAvailablityTime: 
            if(object.startTime<=startTime<=object.endTime):
                return False
            if(object.startTime<=endTime<=object.endTime):
                return False   
        return True

    def addBusy(self,ilutz):
        self.unAvailablityTime.append(ilutz)
    def removeBusy(self,ilutz):
        self.unAvailablityTime.remove(ilutz)