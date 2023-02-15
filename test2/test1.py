import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

lenx = []
listy = []
color = ['c', 'b', 'g', 'r', 'm', 'y', 'k', 'w']

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x[random.randrange(%d)]" % i,"from __main__ import random, x")
    x = list(range(i))
    list_time = t.timeit(number=1000)
    print("%d, %10.3f" % (i, list_time))
    lenx.append(i)
    listy.append(list_time)
    ax = plt.gca()
    # 去掉边框
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # 移位置 设为原点相交
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    listdot = plt.scatter(lenx, listy, c=color[3], edgecolors='r', label='list')
    plt.xlabel('lenth(list)')
    plt.ylabel('time(/s)')
    plt.title('List_index')
    plt.legend()
    plt.show()
