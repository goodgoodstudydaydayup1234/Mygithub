"""
线程
"""
import time
import threading


def timecount(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__, '消耗', end-start)
    return fun


def prt():
    print('hello')
    time.sleep(1)


# @timecount
# def q():
#     for i in range(5):
#         prt()


@timecount
def main():
    list1 = []
    for i in range(5):
        t = threading.Thread(target=prt)
        t.start()
        list1.append(t)
        # t.join()
    # print(list1)
    # 线程执行和进程一样，没有顺序，如果线程很多，
    # 不一定是最后一个开的线程最后执行完，所以list[4]不一定最后执行。
    # list1[4].join()
    for i in list1:
        i.join()


if __name__ == '__main__':
    main()
    # q()












