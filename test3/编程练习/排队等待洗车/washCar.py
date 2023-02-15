from queueText import Queue
from Task import Task

import random

class WashingCar: # 洗车店
    def __init__(self,ppm):
        self.carrate = ppm #洗车速度，按车辆类型区分洗车速度
        self.cuurentTask = None # 开始任务，刚开始没有任务，为None
        self.timeRemaining = 0 # 剩余时间
    
    def tick(self):
        if self.cuurentTask != None: #存在洗车任务
            self.timeRemaining -= 1 # 剩余时间-1
            if self.timeRemaining <= 0: # 剩余时间为0的时候
                self.cuurentTask = None # 把开始洗车任务置为空闲None

    def busy(self): # 查看当前是否忙碌，是否有洗车任务
        if self.cuurentTask != None: # 有洗车任务返回True
            return True
        else: # 没有任务返回False
            return False                  

    def startNext(self,newtask): # 开始下一个车
        self.cuurentTask = newtask # 开始下一个任务
        # 剩余时间 = 车辆类型 x 60 x 此类型车辆的洗车速度
        self.timeRemaining = newtask.getCarClass()*60*self.carrate

# numseconds 模拟洗车时间，minutesPercar 模拟车辆数量
def simulation(numseconds, minutesPercar):# 模拟
    washing = WashingCar(minutesPercar) #初始化洗车店
    carsQueue = Queue() # 初始化洗车队列
    waitingtimes = [] # 洗车时间列表

    for currentSecond in range(numseconds):
        if newwashingTask():
            task = Task(currentSecond) # 初始化洗车任务
            carsQueue.enqueue(task) # 洗车任务加入队列，等待进入洗车店
        if (not washing.busy()) and (not carsQueue.isEmpty()): # 没有洗车任务并且洗车任务队列不为空
            nexttast = carsQueue.dequeue() # 新洗车任务
            waitingtimes.append(nexttast.waitTime(currentSecond))
            washing.startNext(newtask=nexttast) # 开始新洗车任务
        washing.tick() # 洗车完成
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average wait %6.2f secs %3d tasks remaining." % (averageWait, carsQueue.size()))

def newwashingTask():# 新建清洗任务
    range = random.randrange(1,361) # 生成1-361之间的随机数
    if range == 360: # 随机数等于360时，新建洗车任务成功
        return True
    else: # 不等于360时，不创建洗车任务
        return False    


if __name__ == '__main__':

    for i in range(10):
        simulation(3600, 10)