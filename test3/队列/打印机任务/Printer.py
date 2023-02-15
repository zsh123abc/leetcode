# 打印机
# 需要检查当前是否有待完成的任务。如果有，那么打印机就处于工作状态
# 并且其工作所需的时间可以通过要打印的页数来计算。其构造方法会初始化打印速度，即每分钟打印多少页
# tick 方法会减量计时，并且在执行完任务之后将打印机设置成空闲状态

class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm#分页数
        self.currenTask = None#当前是否有任务
        self.timeRemaining = 0#剩余
    def tick(self):#打印机打印，打印完进入空闲状态
        if self.currenTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currenTask = None
    def busy(self):#打印机是否空闲
        if self.currenTask != None:
            return True
        else:
            return False
    def startNext(self,newtask):
        self.currenTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate