"""
时间消耗装饰器
"""
import time


def timecount(f):
    def tc():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__, '消耗', end-start)
    return tc

@timecount
def getfromlist():
    list1 = [x for x in range(100000)]
    print(list1.index(9999))

@timecount
def getfromgeberator():
    g1 = (x for x in range(100000))
    index = 0
    while True:
        try:
            result = next(g1)
            if result == 99999:
                print(index)
                break
            index += 1

        except StopIteration as e:
            print('没有找到')


getfromlist()
getfromgeberator()

