import time

def sumOfN(n):
    start = time.time()
    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i 
    end = time.time()

    return theSum,end-start    

def sumOfN3(n):
    start = time.time()
    theSum = (n*(n+1))/2
    end = time.time()
    return theSum,end-start

for i in range(5):
        print("Sum is %d required %10.7f seconds" % sumOfN(10000))

print('---------------------------')
for i in range(5):
        print("Sum is %d required %10.7f seconds" % sumOfN3(2000000))        



def test1():
    l = []
    for i in range(1000):
            l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))


