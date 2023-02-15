# 任务
import random
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)#生成随机数
    def getStamp(self):
        return self.timestamp
    def getPages(self):#获取随机数
        return self.pages

    def waitTime(self,currenttime):#等待时间
        return currenttime - self.timestamp      