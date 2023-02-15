import random
#洗车任务
class Task:
    def __init__(self ,time):
        self.time = time #洗车时间
        self.carClass = random.randrange(1,4)#随机生成1-3，模拟车辆类型
    def getTime(self):#洗车时间
        return self.time

    def getCarClass(self):#车辆类型
        return self.carClass    

    def waitTime(self ,currenttime):#等待时间
        return currenttime - self.getTime()