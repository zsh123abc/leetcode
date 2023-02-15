class Printer:#打印机
    def __init__(self,ppm):
        self.pagerate = ppm#自定义每分钟打印页数
        self.curretTask = None#初始打印任务
        self.timeRemaining = 0#需要等待时间，任务倒计时

    def tick(self):
        # 打印1秒
        if self.curretTask != None:
            self.timeRemaining = self.timeRemaining-1#开始打印后，减少打印需等待时间

            if self.timeRemaining < 1:#打印等待时间为0，打印完成
                self.curretTask = None#打印机置为空闲

    def busy(self):#查看打印机是否在打印中
        if self.curretTask == None:
            return False
        else:
            return True    

    def startNext(self, newtask):#开始下一个任务
        self.curretTask = newtask
        self.timeRemaining += newtask.getPages()*60/self.pagerate#当前任务剩余时间


import random
class Task:#打印任务
    
    def __init__(self,time):
        self.timestamp = time#记录提交任务时间戳
        self.pages = random.randrange(1,21)#随机生成打印页数，1-20之间

    def getStamp(self):
        return self.timestamp
    def getPages(self):#获取当前任务打印页数
        return self.pages
    def waitTime(self,currenttime):#任务在队列中的等待时间
        return currenttime - self.timestamp
    pass


from queueText import Queue
class PrintQueue:#打印队列

    def simulation(self, numSeconds, pagesPerMinute):#numSeconds打印机工作时间,pagesPerMinute每分钟打印页数
        printer = Printer(pagesPerMinute)
        queue = Queue()
        waitingtimes = []
        for currentSeconds in range(numSeconds):
            if self.newPrintTask():
                task = Task(currentSeconds)
                queue.enqueue(task)

            if (not printer.busy()) and (not queue.isEmpty()):
                newtask = queue.dequeue()

                waitingtimes.append(newtask.waitTime(currentSeconds))

                printer.startNext(newtask)
            printer.tick()
        
        averageWait = sum(waitingtimes)/len(waitingtimes)#平均等待时间
        # 剩余时间为0的就表示当前打印任务在规定时间内完成
        print('平均等待时间为: %6.2f s  任务剩余时间: %3d '%(averageWait,queue.size()))


    def newPrintTask(self):
        num = random.randrange(1,181)
        if num == 180:
            return True
        else:
            return False    

if __name__ == '__main__':
    printQueue = PrintQueue()
    for i in range(10):
        # 打印机工作60分钟，每分钟打印10页
        printQueue.simulation(3600,2)#自定义打印机工作时间和每分钟打印页数
