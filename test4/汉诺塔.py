# height盘子数量，fromPole从哪个盘子移，toPole经过哪个盘子，withPole移动到哪个盘子
def hanoi(height, a, b, c):
    if height>0:#移完所有盘子
        hanoi(height-1,a,c,b)
        moveDisk(height,a,c)
        
        hanoi(height-1,b,a,c)
def moveDisk(h,fp, tp):
    print("第%d 个盘子 从%d 移到 %d\n" % (h,fp, tp))

import time
 
start_time = time.time()
hanoi(40, 1,2,3)     
end_time = time.time()
print("程序执行了%f秒"%(end_time - start_time))