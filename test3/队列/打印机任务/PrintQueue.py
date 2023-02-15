# 打印队列
from queueText import Queue
from Printer import Printer
from Task import Task
import random
# numSeconds模拟打印多久，pagesPerMinute一分钟打印多少页
def simulation(numSeconds, pagesPerMinute):
      labprinter = Printer(pagesPerMinute)
      printQueue = Queue()
      waitingtimes = []

      for currentSecond in range(numSeconds):

        if newPrintTask():#加入新打印机任务
             task = Task(currentSecond)
             printQueue.enqueue(task)#加入打印机任务到队列
        #打印机处于空闲状态，队列为空
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
              nexttask = printQueue.dequeue()#拿出队列中第一个任务
              waitingtimes.append(nexttask.waitTime(currentSecond))
              labprinter.startNext(nexttask)

        labprinter.tick()

      averageWait=sum(waitingtimes)/len(waitingtimes)
      print("Average Wait %6.2f secs %3d tasks remaining."\
                      %(averageWait, printQueue.size()))



def newPrintTask():#新打印机任务
      num = random.randrange(1, 181)
      if num == 180:#等于180任务生成成功
          return True
      else:
          return False


for i in range(10):
    simulation(3600,10)